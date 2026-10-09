/* Evidence-separated RF power comparison; no physiological outcome model. */
(() => {
  'use strict';
  const data = window.RF_POWER_ATLAS, records = data.devices;
  const $ = id => document.getElementById(id);
  const escape = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const num = value => value == null ? 'Unknown' : Number(value).toLocaleString(undefined, {maximumFractionDigits:2});
  const watts = value => value == null ? 'Not disclosed' : `${num(value)} W`;
  const sources = new Map(data.sources.map(s => [s.id, s]));
  const documented = r => ['FDA specification','Manufacturer manual','Numeric FDA bench result','Manufacturer specification'].includes(r.basis);
  let expanded = false;
  const explanations = {
    documented:'Current manufacturer/manual and FDA RF maximum specifications. Loads and rating conventions differ. Historical conflicts and seller/marketing maxima remain unranked in this view.',
    treatment:'Highest explicitly disclosed selectable setting. A hardware maximum is not substituted when the setting-specific value is missing.',
    claims:'Published RF or handle-power maxima, including claims. This is a headline comparison: source quality, output convention and intended treatment area differ.',
    measured:'Only exact numeric RF bench results disclosed in the corpus. Passing accuracy tests without publishing the measured value does not supply a bar.',
    input:'Input consumption and adapter/charging capacity, as labeled. These are different electrical quantities and are not RF output. Read each row’s label.',
    battery:'Nominal average whole-device energy budget from verified cell voltage, capacity and stated runtime. “Up to” runtime does not define a full-power RF test.'
  };
  function metric(r,m) {
    if(m==='documented') return documented(r) ? r.rf_max_w : null;
    if(m==='treatment') return r.treatment_max_w;
    if(m==='claims') return r.rf_max_w;
    if(m==='measured') return r.measured_w;
    if(m==='input') return r.input_w;
    if(m==='battery') return r.average_total_w;
    return null;
  }
  function inCategory(r,c) {
    if(c==='all') return true;
    if(c==='home') return ['Home face RF','Home body RF','Generic handheld RF'].includes(r.category);
    if(c==='generic') return r.category.startsWith('Generic');
    return r.category===c;
  }
  function detail(r) {
    const links=r.source_ids.map(id => {
      const s=sources.get(id);
      if(!s) return `<a href="index.html#doc21">${escape(id)} · ${id.startsWith('U')?'Pasted lead':'Prior census'}</a>`;
      return `<a href="${escape(s.url)}" target="_blank" rel="noopener">${escape(id)} · ${escape(s.title)}</a>${s.local ? ` <a href="${escape(s.local)}">Preserved ${s.local.endsWith('.pdf')?'PDF':'capture'}</a>` : ''}`;
    }).join('<br>');
    return `<div class="detailgrid"><div><p><b>${escape(r.category)} · checked ${escape(r.checked)}</b></p><p>${escape(r.notes)}</p><p><b>Carrier / wavelength:</b> ${escape(r.frequency)}<br><b>Power evidence:</b> ${escape(r.basis)}<br><b>Clearance:</b> ${escape(r.clearance)}</p></div><div><p><b>Source trail</b><br>${links}</p>${r.prior_source_ids?`<p>Earlier source IDs: ${escape(r.prior_source_ids.join(' '))}. <a href="data/rf_sources_2026-10-02.json">Prior source registry</a></p>`:''}<p><a href="index.html#doc19">Power method and limits</a></p></div></div>`;
  }
  function render() {
    const m=$('metric').value,c=$('category').value,q=$('search').value.toLowerCase().trim();
    const selected=records.filter(r=>inCategory(r,c)&&(!q||[r.brand,r.model,r.notes,r.frequency,r.clearance,r.load_ohm,r.basis].join(' ').toLowerCase().includes(q))).sort((a,b)=>{
      const av=metric(a,m),bv=metric(b,m);
      if(av==null&&bv!=null)return 1;if(bv==null&&av!=null)return -1;
      return (bv??0)-(av??0)||a.brand.localeCompare(b.brand)||a.model.localeCompare(b.model);
    });
    const known=selected.filter(r=>metric(r,m)!=null),max=Math.max(1,...known.map(r=>metric(r,m)));
    $('explain').textContent=explanations[m];
    $('status').textContent=`${selected.length} records shown · ${known.length} numeric · ${selected.length-known.length} unranked for this quantity`;
    $('chart-note').textContent=`Linear scale · watts · ${max.toLocaleString()} W maximum in this selection. Bars compare this quantity only; they do not show efficacy or power absorbed by dermis.`;
    $('bars').innerHTML=(expanded?known:known.slice(0,18)).map(r=>{
      const v=metric(r,m),kind=m==='input'?'input':m==='battery'?'battery':!documented(r)?'claim':'';
      return `<div class="barrow"><div class="barlabel"><b>${escape(r.brand)} ${escape(r.model)}</b><small>${escape(m==='input'?r.input_kind:m==='battery'?`${num(r.battery_wh)} Wh ÷ ${r.runtime_min} min · total draw estimate`:r.basis)}${r.load_ohm!=null&&['documented','measured','treatment','claims'].includes(m)?` · ${r.load_ohm} Ω`:''}</small></div><div class="track"><div class="bar ${kind}" style="width:${v/max*100}%"></div></div><div class="val">${num(v)} W</div></div>`;
    }).join('') || '<p>No numerical value established for this selection. The ledger below retains the unknown records.</p>';
    $('expand').hidden=known.length<=18; $('expand').textContent=expanded?'Show first 18 numeric records':'Show every numeric record';
    $('rows').innerHTML=selected.map(r=>`<tr><td class="model"><button class="detail" data-id="${r.id}" aria-expanded="false" aria-controls="detail-${r.id}">${escape(r.brand)} ${escape(r.model)}</button><small>${escape(r.category)} · ${escape(r.checked)}</small></td><td>${escape(r.rf_label)}<small>${escape(r.basis)}${r.treatment_max_w!=null?`<br>Highest setting: ${watts(r.treatment_max_w)}`:''}</small></td><td>${watts(r.measured_w)}<small>${r.load_ohm==null?'Load undisclosed':`${r.load_ohm} Ω ${r.measured_w==null?'specification / validation':'bench result'}`}</small></td><td>${watts(r.input_w)}<small>${escape(r.input_kind)}</small></td><td>${r.battery_wh!=null?`${num(r.battery_wh)} Wh`:r.battery_mah!=null?`${r.battery_mah} mAh; voltage unknown`:'Not established'}<small>${r.runtime_min!=null?`${r.runtime_min} min stated runtime<br>`:''}${r.average_total_w!=null?`${watts(r.average_total_w)} nominal total average`:'No total-draw estimate'}</small></td><td>${escape(r.temperature)}<small>${escape(r.clearance)}</small></td></tr><tr class="detailrow" id="detail-${r.id}" hidden><td colspan="6">${detail(r)}</td></tr>`).join('');
    $('empty').hidden=selected.length>0;
  }
  $('rows').addEventListener('click',e=>{const b=e.target.closest('button[data-id]');if(!b)return;const row=$(`detail-${b.dataset.id}`);row.hidden=!row.hidden;b.setAttribute('aria-expanded',String(!row.hidden));});
  for(const id of ['search','category','metric'])$(id).addEventListener('input',()=>{expanded=false;render();});
  $('expand').addEventListener('click',()=>{expanded=!expanded;render();});
  $('total').textContent=records.length;
  const hash=location.hash.slice(1);if(hash==='generic')$('category').value='generic';if(hash==='battery')$('metric').value='battery';
  window.RFPowerAtlasTest={metric,inCategory,records};
  render();
})();
