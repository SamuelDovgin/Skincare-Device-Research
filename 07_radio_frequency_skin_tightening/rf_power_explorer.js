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
      return `<a href="${escape(s.url)}" target="_blank" rel="noopener">${escape(id)} · ${escape(s.title)}</a>${s.local ? ` <a href="${escape(s.local)}">Preserved ${s.local.endsWith('.pdf')?'PDF':s.local.endsWith('.txt')?'excerpt':'capture'}</a>` : ''}`;
    }).join('<br>');
    const curve=r.curve_data?.length?`<p><b>Manual plot read-offs*:</b> ${r.curve_data.map(p=>`${num(p.rf_w)} W at ${num(p.load_ohm)} Ω`).join(' · ')}<br><small>${escape(r.curve_label||'Approximate visual read-offs; not bench measurements.')}</small></p>`:'';
    return `<div class="detailgrid"><div><p><b>${escape(r.category)} · checked ${escape(r.checked)}</b></p><p>${escape(r.notes)}</p><p><b>Carrier / wavelength:</b> ${escape(r.frequency)}<br><b>Power evidence:</b> ${escape(r.basis)}<br><b>Confidence:</b> ${escape(r.confidence||'Not separately rated')}<br><b>Clearance:</b> ${escape(r.clearance)}</p>${curve}</div><div><p><b>Source trail</b><br>${links}</p>${r.prior_source_ids?`<p>Earlier source IDs: ${escape(r.prior_source_ids.join(' '))}. <a href="data/rf_sources_2026-10-02.json">Prior source registry</a></p>`:''}<p><a href="index.html#doc19">Power method and limits</a></p></div></div>`;
  }
  function renderCurves(selected) {
    const series=selected.filter(r=>Array.isArray(r.curve_data)&&r.curve_data.length).map(r=>({...r,curve_data:[...r.curve_data].sort((a,b)=>a.load_ohm-b.load_ohm)}));
    if(!series.length){$('curve-chart').innerHTML='<p>No manual load curves match the current search and device class. Clear the search or select a broader class.</p>';return;}
    const colors=['#633b96','#b45f22','#087e8b','#bb3e72','#607d28','#475c9b'];
    const width=780,height=370,left=76,right=22,top=24,bottom=64,plotW=width-left-right,plotH=height-top-bottom;
    const xmax=Math.ceil(Math.max(...series.flatMap(r=>r.curve_data.map(p=>p.load_ohm)))/100)*100;
    const ymax=Math.ceil(Math.max(...series.flatMap(r=>r.curve_data.map(p=>p.rf_w)))/2)*2;
    const x=v=>left+(v/xmax)*plotW,y=v=>top+plotH-(v/ymax)*plotH;
    let svg=`<svg class="curve-svg" viewBox="0 0 ${width} ${height}" role="img" aria-labelledby="curve-svg-title curve-svg-desc"><title id="curve-svg-title">Manufacturer manual RF output versus load</title><desc id="curve-svg-desc">Approximate read-offs from ${series.length} manuals. Asterisk means approximate manual-plot digitization, not a lab result. Axes show load in ohms and output in watts.</desc>`;
    for(let tick=0;tick<=ymax;tick+=Math.max(1,ymax/4)){
      const yy=y(tick);svg+=`<line x1="${left}" y1="${yy}" x2="${width-right}" y2="${yy}" stroke="#e5e0eb"/><text x="${left-12}" y="${yy+4}" text-anchor="end" font-size="12" fill="#606173">${num(tick)}</text>`;
    }
    const xStep=xmax<=300?50:100;
    for(let tick=0;tick<=xmax;tick+=xStep){const xx=x(tick);svg+=`<line x1="${xx}" y1="${top}" x2="${xx}" y2="${top+plotH}" stroke="#f0edf4"/><text x="${xx}" y="${top+plotH+23}" text-anchor="middle" font-size="12" fill="#606173">${tick}</text>`;}
    svg+=`<line x1="${left}" y1="${top+plotH}" x2="${width-right}" y2="${top+plotH}" stroke="#60576b"/><line x1="${left}" y1="${top}" x2="${left}" y2="${top+plotH}" stroke="#60576b"/><text x="${left+plotW/2}" y="${height-12}" text-anchor="middle" font-size="13" fill="#222333">Electrical load (Ω)</text><text transform="translate(20 ${top+plotH/2}) rotate(-90)" text-anchor="middle" font-size="13" fill="#222333">RF output (W*)</text>`;
    series.forEach((r,i)=>{
      const color=colors[i%colors.length],coords=r.curve_data.map(p=>`${x(p.load_ohm)},${y(p.rf_w)}`).join(' ');
      svg+=`<polyline points="${coords}" fill="none" stroke="${color}" stroke-width="2.5" stroke-linejoin="round" stroke-dasharray="7 4"/>`;
      r.curve_data.forEach(p=>{svg+=`<circle cx="${x(p.load_ohm)}" cy="${y(p.rf_w)}" r="5" fill="white" stroke="${color}" stroke-width="2.5"><title>${escape(r.brand)} ${escape(r.model)}: approximately ${num(p.rf_w)} W at ${num(p.load_ohm)} Ω*</title></circle>`;});
    });
    svg+='</svg>';
    const legend=series.map((r,i)=>{
      const ids=r.source_ids.map(id=>{const s=sources.get(id);return s?`<a href="${escape(s.url)}" target="_blank" rel="noopener">${escape(id)} manual/source</a>`:'';}).filter(Boolean).join(' · ');
      return `<div class="curve-key"><span class="curve-swatch" style="background:${colors[i%colors.length]}"></span><span><b>${escape(r.brand)} ${escape(r.model)}</b><span class="curve-points">${r.curve_data.map(p=>`${num(p.rf_w)} W* @ ${num(p.load_ohm)} Ω`).join(' · ')} · ${ids}</span></span></div>`;
    }).join('');
    $('curve-chart').innerHTML=`<div class="curve-wrap">${svg}</div><div class="curve-legend">${legend}</div><p class="footer">* Visual approximation of printed graph markers. The lines connect only the listed points and should not be read as a continuous verified response curve.</p>`;
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
    renderCurves(selected);
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
