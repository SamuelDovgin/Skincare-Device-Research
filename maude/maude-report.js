(function(){
  "use strict";

  const TOPICS={
    "01_ipl_hair_removal":{
      code:"OHT",
      title:"FDA-reported events in home light hair removal",
      intro:"This shared OHT lane covers consumer IPL and diode/laser-style hair-removal devices. FDA's product code is regulatory, not a perfect technology label, so the brand, model, and narrative must be read before applying a report to a specific device.",
      note:"OHT is shared with the diode-laser page. It is not a count of IPL-only events, and it is not an adverse-event rate."
    },
    "02_diode_laser_hair_removal":{
      code:"OHT",
      title:"FDA-reported events in home light hair removal",
      intro:"The diode-laser page uses the same OHT dataset as the IPL page because FDA groups OTC light-based hair-removal devices in one product code. Brand and narrative review are essential before treating a report as diode-specific.",
      note:"OHT is shared with the IPL page. It includes IPL and diode/laser-style consumer hair-removal devices; the data cannot be split cleanly by code alone."
    },
    "04_red_light_therapy_handheld":{
      code:"OHS",
      title:"FDA-reported events in OTC light / LED wrinkle devices",
      intro:"OHS is the FDA product-code lane for OTC light-based wrinkle reduction. It includes LED masks and handheld light systems, so reports can reveal real-world themes such as skin irritation, discoloration, eye symptoms, and device-user interaction problems.",
      note:"OHS is broader than photobiomodulation research and does not prove that every report involved a red/NIR LED device."
    },
    "07_radio_frequency_skin_tightening":{
      code:"PAY",
      title:"FDA-reported events in OTC radiofrequency wrinkle devices",
      intro:"PAY is the FDA product-code lane for non-invasive OTC RF wrinkle-reduction devices. The current public report count is small, so this view is most useful for individual-device identity and reported problem review—not category-wide risk estimates.",
      note:"A small report count may reflect limited exposure, reporting behavior, or the relatively new/narrow product-code lane; it is not evidence of zero risk."
    },
    "10_microneedling_collagen_induction":{
      code:"QAI",
      title:"FDA-reported events in powered microneedling",
      intro:"QAI covers powered microneedling devices used to mechanically puncture skin for aesthetic use. Reports are especially useful here for separating device faults from procedure, sterility, training, off-label, and patient-selection issues.",
      note:"QAI is a professional medical-device lane. These reports should not be generalized to superficial cosmetic rollers or to RF microneedling without reading the exact device and narrative."
    },
    "11_hifu_skin_tightening":{
      code:"OHV",
      title:"FDA-reported events in aesthetic focused ultrasound",
      intro:"OHV covers focused-ultrasound aesthetic systems, including facial MFU/HIFU and some body-contouring devices. The code is broader than home facial HIFU, so the brand, model, treatment context, and narrative are necessary for interpretation.",
      note:"OHV reports mostly represent professional systems and should not be read as evidence that a consumer device has the same output or risk profile."
    }
  };

  const esc=(value)=>String(value==null?"":value).replace(/[&<>"']/g,(c)=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[c]));
  const arr=(value)=>Array.isArray(value)?value.filter(Boolean):[];
  const join=(value,empty="Not provided")=>arr(value).join(" · ")||empty;
  const fmtDate=(value)=>{
    const s=String(value||"");
    if(/^\d{8}$/.test(s)) return `${s.slice(4,6)}/${s.slice(6,8)}/${s.slice(0,4)}`;
    return s||"Not provided";
  };
  const topicKey=()=>location.pathname.split("/").filter(Boolean)[0]||"";

  function buildSection(config){
    const section=document.createElement("section");
    section.className="doc maude-doc";
    section.id="maude";
    section.setAttribute("aria-labelledby","maude-title");
    section.innerHTML=`
      <span class="maude-kicker">Post-market signal · FDA MAUDE</span>
      <h1 id="maude-title">${esc(config.title)}</h1>
      <p class="maude-lead">${esc(config.intro)}</p>
      <div class="maude-notice"><b>Read this correctly:</b> These are reports submitted to FDA, not confirmed causal findings or event rates. A report can contain multiple devices, patients, coded terms, follow-ups, and redacted or incomplete narrative information. <a href="../markdown-viewer.html?file=maude/README.md">Read the method and limitations →</a></div>
      <div id="maudeStatus" class="maude-foot">Loading the local ${esc(config.code)} snapshot…</div>
      <div class="maude-toolbar" aria-label="Filter reported events">
        <label class="maude-field">Search records<input id="maudeSearch" type="search" placeholder="Brand, model, symptom, problem, or narrative" autocomplete="off"></label>
        <label class="maude-field">Event type<select id="maudeEvent"><option value="">All event types</option></select></label>
        <label class="maude-field">Sort<select id="maudeSort"><option value="newest">Newest first</option><option value="oldest">Oldest first</option><option value="brand">Brand / model</option></select></label>
      </div>
      <div id="maudeSummary" class="maude-summary" aria-live="polite"></div>
      <div id="maudeInsight" class="maude-insight"></div>
      <div class="maude-results-head"><h2>Reported records</h2><span id="maudeCount" class="maude-count"></span></div>
      <div id="maudeRecords" class="maude-records"></div>
      <div id="maudeEmpty" class="maude-empty" hidden>No matching reports in this local snapshot. Try a broader search or clear the filters.</div>
      <details class="maude-method"><summary>What this panel preserves</summary><ul><li>FDA MDR report key and direct FDA detail link.</li><li>Report date, event type, source/reporter fields, brand, model, manufacturer, and 510(k)/PMA field when present.</li><li>FDA patient-problem and device-problem terms, outcomes, device availability/evaluation fields, follow-up flags, and the public narrative.</li><li>Repeated coded terms within one report are shown once, but separate reports and multiple device/patient entries are retained.</li></ul><p>${esc(config.note)}</p></details>`;
    return section;
  }

  function navButton(){
    const wrap=document.createElement("div");
    wrap.innerHTML='<h3>Post-market</h3><button class="navbtn" data-t="maude">🧾 FDA-reported events</button>';
    return wrap;
  }

  function recordSearchText(record){
    return [record.mdr_report_key,record.event_type,record.report_source,record.reporter_occupation,record.pma_510k,...arr(record.brand_names),...arr(record.model_numbers),...arr(record.manufacturers),...arr(record.patient_problems),...arr(record.device_problems),...arr(record.outcomes),...arr(record.narratives)].join(" ").toLowerCase();
  }

  function renderRecord(record){
    const brand=join(record.brand_names,"Unnamed device");
    const model=join(record.model_numbers,"Model not provided");
    const patient=join(record.patient_problems,"No patient-problem term provided");
    const device=join(record.device_problems,"No device-problem term provided");
    const narrative=join(record.narratives,"No public narrative provided");
    const tags=[record.event_type,...arr(record.patient_problems).slice(0,4),...arr(record.device_problems).slice(0,3)];
    return `<details class="maude-record"><summary><div class="maude-record-top"><span class="maude-record-title">${esc(brand)} <span style="font-weight:400;color:var(--muted)">· ${esc(model)}</span></span><span class="maude-record-date">Received ${esc(fmtDate(record.date_received))}</span></div><div class="maude-record-meta">${tags.filter(Boolean).map((tag,i)=>`<span class="maude-tag${i===0?" event":""}">${esc(tag)}</span>`).join("")}</div></summary><div class="maude-record-body"><div class="maude-detail-grid"><dl><dt>FDA report</dt><dd>${esc(record.mdr_report_key||"Not provided")}</dd></dl><dl><dt>Event type</dt><dd>${esc(record.event_type||"Not provided")}</dd></dl><dl><dt>Patient-problem terms</dt><dd>${esc(patient)}</dd></dl><dl><dt>Device-problem terms</dt><dd>${esc(device)}</dd></dl><dl><dt>Source / reporter</dt><dd>${esc(arr(record.source_type).join(" · ")||record.report_source||"Not provided")}${record.reporter_occupation?` · ${esc(record.reporter_occupation)}`:""}</dd></dl><dl><dt>Manufacturer / 510(k) or PMA</dt><dd>${esc(join(record.manufacturers))}${record.pma_510k?` · ${esc(record.pma_510k)}`:""}</dd></dl></div><b>Public narrative</b><div class="maude-narrative">${esc(narrative)}</div><a class="maude-open" href="${esc(record.detail_url)}" target="_blank" rel="noopener">Open this report at FDA ↗</a></div></details>`;
  }

  function run(){
    const key=topicKey(), config=TOPICS[key];
    if(!config) return;
    if(!document.querySelector('link[href$="/maude/maude-report.css"],link[href="../maude/maude-report.css"]')){
      const css=document.createElement("link"); css.rel="stylesheet"; css.href="../maude/maude-report.css"; document.head.appendChild(css);
    }
    const main=document.querySelector(".main"), side=document.querySelector(".side");
    if(!main||!side||document.getElementById("maude")) return;
    const section=buildSection(config);
    const start=main.querySelector("#start");
    if(start) start.after(section); else main.prepend(section);
    const firstHeading=side.querySelector("h3");
    side.insertBefore(navButton(),firstHeading||null);
    const button=side.querySelector('[data-t="maude"]');
    button.addEventListener("click",()=>{
      if(typeof window.show==="function") window.show("maude");
      else { section.classList.add("active"); location.hash="maude"; }
    });
    const dataUrl=`../maude/data/maude_${config.code.toLowerCase()}.json`;
    fetch(dataUrl).then(response=>{if(!response.ok) throw new Error(`HTTP ${response.status}`);return response.json();}).then(payload=>init(section,payload,config)).catch(error=>{
      const status=section.querySelector("#maudeStatus");
      status.textContent=`The local ${config.code} snapshot could not be loaded (${error.message}). Open the served site or retry; the page does not expose the underlying source file as a reader control.`;
    });
    if(location.hash==="#maude"&&typeof window.show==="function") window.show("maude");
  }

  function init(section,payload,config){
    const metadata=payload.metadata||{}, records=arr(payload.records).map(record=>({...record,_search:recordSearchText(record)}));
    const status=section.querySelector("#maudeStatus");
    status.innerHTML=`FDA product code <b>${esc(config.code)}</b> · ${esc(metadata.record_count||records.length)} local records · captured ${esc(metadata.captured_at||"not provided")} · API dataset update ${esc(metadata.api_last_updated||"not provided")} · <a href="${esc(metadata.source_url||"https://open.fda.gov/data/maude/")}" target="_blank" rel="noopener">official openFDA query ↗</a>`;
    const eventSelect=section.querySelector("#maudeEvent");
    [...new Set(records.map(r=>r.event_type).filter(Boolean))].sort().forEach(value=>{const option=document.createElement("option");option.value=value;option.textContent=value;eventSelect.appendChild(option);});
    const search=section.querySelector("#maudeSearch"), event=eventSelect, sort=section.querySelector("#maudeSort");
    const render=()=>{
      const q=search.value.trim().toLowerCase(), eventValue=event.value;
      let visible=records.filter(record=>(!q||record._search.includes(q))&&(!eventValue||record.event_type===eventValue));
      visible.sort((a,b)=>{if(sort.value==="oldest") return String(a.date_received).localeCompare(String(b.date_received));if(sort.value==="brand") return join(a.brand_names).localeCompare(join(b.brand_names));return String(b.date_received).localeCompare(String(a.date_received));});
      section.querySelector("#maudeRecords").innerHTML=visible.map(renderRecord).join("");
      section.querySelector("#maudeEmpty").hidden=visible.length>0;
      section.querySelector("#maudeCount").textContent=`Showing ${visible.length} of ${records.length} report records`;
    };
    const eventCounts=metadata.event_counts||{};
    section.querySelector("#maudeSummary").innerHTML=[
      [records.length,"local report records"],
      [eventCounts.Injury||0,"coded Injury events"],
      [eventCounts.Malfunction||0,"coded Malfunction events"],
      [new Set(records.flatMap(r=>arr(r.brand_names))).size,"named brand values"]
    ].map(([value,label])=>`<div class="maude-stat"><b>${esc(value)}</b><span>${esc(label)}</span></div>`).join("");
    const patient=Object.entries(metadata.patient_problem_counts||{}).sort((a,b)=>b[1]-a[1]).slice(0,10);
    const device=Object.entries(metadata.device_problem_counts||{}).sort((a,b)=>b[1]-a[1]).slice(0,8);
    section.querySelector("#maudeInsight").innerHTML=`<h3>Most frequent coded terms in this snapshot</h3><div class="maude-chipset">${patient.map(([label,count])=>`<span class="maude-chip">${esc(label)} <b>${esc(count)}</b></span>`).join("")||'<span class="maude-foot">No patient-problem terms were supplied.</span>'}</div><h3 style="margin-top:12px">Device/problem terms</h3><div class="maude-chipset">${device.map(([label,count])=>`<span class="maude-chip">${esc(label)} <b>${esc(count)}</b></span>`).join("")||'<span class="maude-foot">No device-problem terms were supplied.</span>'}</div>`;
    [search,event,sort].forEach(control=>control.addEventListener("input",render));
    [event,sort].forEach(control=>control.addEventListener("change",render));
    render();
  }

  if(document.readyState==="loading") document.addEventListener("DOMContentLoaded",run); else run();
})();
