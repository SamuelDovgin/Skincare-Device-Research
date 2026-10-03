/* Evidence filters change visibility, never clinical tiers or predicted outcomes. */
(function(root,factory){'use strict';const model=factory();if(typeof module==='object'&&module.exports)module.exports=model;else root.RFCollagenModel=model;})(typeof globalThis!=='undefined'?globalThis:this,function(){
  'use strict';
  const order={'A':0,'A-':1,'B':2,'C':3,'D':4,'Clinic':5};
  function matches(d,f={}){
    if(d.scope==='clinic')return false;
    if(f.direct&&!d.directHuman)return false;
    if(f.numeric&&!d.numericControl)return false;
    if(f.references===false&&d.reference)return false;
    if(f.search&&!`${d.name} ${d.tier} ${d.kind} ${d.frequency}`.toLowerCase().includes(f.search.toLowerCase()))return false;
    return true;
  }
  function filter(devices,f){return devices.filter(d=>matches(d,f)).sort((a,b)=>order[a.tier]-order[b.tier]);}
  function shortlist(devices,f={}){
    const eligible=filter(devices,f);const cb=eligible.find(d=>d.id==='currentbody'),newa=eligible.find(d=>d.id==='newa');
    if(cb)return {device:cb,reason:'Practical first shortlist: CurrentBody ST030',text:'Transparent thermal controls and current U.S. identity. Its reviewed FDA summary reports no new subject-device clinical testing. This is a buying judgment, not proven efficacy superiority.'};
    if(newa)return {device:newa,reason:'Direct clinical evidence anchor: original NEWA',text:'Stronger direct human outcome support in this lineup, but uncontrolled and historical/model-specific. Confirm that a currently sold unit actually matches the evidence and local IFU.'};
    const bridge=eligible.find(d=>d.id==='sensilift');
    if(bridge)return {device:bridge,reason:'Controlled-RF alternative: Sensilift Pro ST300',text:'Good technical/regulatory bridge; no new subject-device clinical trial in the reviewed summary.'};
    return {device:null,reason:'No A/A− or documented bridge candidate matches these filters',text:'Other visible entries retain their original tiers. Missing evidence does not prove ineffectiveness; the filter cannot establish a best device.'};
  }
  function chain(d){return [
    {label:'1. Deliver RF',status:d.regulatoryBridge?'Documented bench/label record':'Partial or manufacturer record',body:d.output+' '+d.contact},
    {label:'2. Control tissue heating',status:d.numericControl?'Skin control documented; dermal dose unknown':'Thermal dose unresolved',body:d.control+' '+d.thermal},
    {label:'3. Establish collagen change',status:'Human collagen amount unquantified',body:d.collagen},
    {label:'4. Show useful human change',status:d.directHuman?'Direct study, limitations apply':d.regulatoryBridge?'Indirect regulatory bridge':'Indirect, lineage or claimed',body:d.human}
  ];}
  function validate(data){
    const failures=[],ids=new Set();
    for(const d of data.devices){
      if(ids.has(d.id))failures.push('duplicate '+d.id);ids.add(d.id);
      if(!(d.tier in order))failures.push('invalid tier '+d.id);
      if(typeof d.directHuman!=='boolean'||typeof d.numericControl!=='boolean')failures.push('missing evidence flag '+d.id);
      if(!d.sources.length||d.sources.some(s=>!data.sources[s]))failures.push('missing source '+d.id);
      if(!d.human||!d.collagen||!d.control)failures.push('missing endpoint '+d.id);
    }
    for(const [key,c] of Object.entries({...data.professionalDecisions,...data.homeDecisions})){
      if(!c.title||!c.text||!c.devices.length)failures.push('missing service decision '+key);
      if(c.devices.some(id=>!ids.has(id))||c.sources.some(id=>!data.sources[id]))failures.push('unresolved service reference '+key);
    }for(const [id,features] of Object.entries(data.homeFeatures||{})){if(!ids.has(id)||features.length!==data.homeFeatureLabels.length)failures.push('invalid home feature record '+id);}for(const c of Object.values(data.homeDecisions||{})){if(c.devices.some(id=>!data.homeFeatures[id]))failures.push('missing home comparison features');}return failures;
  }
  return Object.freeze({filter,shortlist,chain,validate,matches});
});
