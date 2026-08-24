#!/usr/bin/env node
/* Build the auditable ingredient-only pair matrix from the Stack Lab rule engine. */

const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..');
const htmlPath = path.join(root, '13_combined_skincare_regimen', 'skincare_stack_lab.html');
const outputPath = path.join(root, '13_combined_skincare_regimen', 'data', 'ingredient_pair_research_ledger.csv');

function loadRuleEngine() {
  const html = fs.readFileSync(htmlPath, 'utf8');
  let script = html.match(/<script>\s*([\s\S]*?)\s*<\/script>/)[1];
  const marker = "    loadState();if(state.preset==='foundation'&&!allOccurrences().length)state.schedule=foundationSchedule(false);renderAll();renderPairGrids();";
  const markerIndex = script.indexOf(marker);
  if (markerIndex < 0) throw new Error('Could not find Stack Lab startup marker');
  script = script.slice(0, markerIndex) + '    window.__ledger={ITEMS,INGREDIENT_IDS,SOURCES,findBaseRule};\n  })();';

  const noop = () => {};
  const fakeElement = {
    addEventListener: noop, removeEventListener: noop, querySelector: () => fakeElement,
    querySelectorAll: () => [], classList: {toggle: noop, add: noop, remove: noop},
    style: {}, setAttribute: noop, removeAttribute: noop, focus: noop, contains: () => false,
    checked: false, value: '', textContent: '', innerHTML: '', open: false
  };
  const sandbox = {
    window: {},
    document: {querySelector: () => fakeElement, querySelectorAll: () => [], createElement: () => fakeElement, body: fakeElement},
    localStorage: {getItem: () => null, setItem: noop},
    location: {search: ''}, URLSearchParams, matchMedia: () => ({matches: false}),
    requestAnimationFrame: noop, setTimeout: noop, clearTimeout: noop,
    confirm: () => false, console
  };
  vm.createContext(sandbox);
  vm.runInContext(script, sandbox, {timeout: 1000});
  return sandbox.window.__ledger;
}

function csvCell(value) {
  const text = value == null ? '' : String(value);
  return /[",\n\r]/.test(text) ? `"${text.replace(/"/g, '""')}"` : text;
}

const {ITEMS, INGREDIENT_IDS, SOURCES, findBaseRule} = loadRuleEngine();
const itemById = new Map(ITEMS.map(item => [item.id, item]));
const rows = [[
  'pair_id', 'left_id', 'left_name', 'right_id', 'right_name',
  'same_session_category', 'minimum_spacing', 'rule_title', 'source_ids', 'proof_links', 'evidence_scope'
]];

for (let i = 0; i < INGREDIENT_IDS.length; i += 1) {
  for (let j = i + 1; j < INGREDIENT_IDS.length; j += 1) {
    const leftId = INGREDIENT_IDS[i];
    const rightId = INGREDIENT_IDS[j];
    const rule = findBaseRule(leftId, rightId);
    const sourceIds = rule.sources || [];
    const proofLinks = sourceIds.map(id => SOURCES[id]?.url || '').filter(Boolean).join('; ');
    rows.push([
      `P${String(rows.length).padStart(3, '0')}`,
      leftId, itemById.get(leftId).name,
      rightId, itemById.get(rightId).name,
      rule.level, rule.minGap || 'none', rule.title,
      sourceIds.join('; '), proofLinks, rule.detail
    ]);
  }
}

fs.writeFileSync(outputPath, rows.map(row => row.map(csvCell).join(',')).join('\n') + '\n', 'utf8');
const unknown = rows.slice(1).filter(row => row[5] === 'unknown').length;
console.log(`WROTE ${outputPath} (${rows.length - 1} pairs; ${unknown} unknown)`);
