/* Shared metadata, deduplication, and portable bibliography functions. */
(function(root){
'use strict';
const str=v=>String(v??'');
const doi=v=>str(v).trim().replace(/^https?:\/\/(?:dx\.)?doi\.org\//i,'').replace(/^doi:\s*/i,'').toLowerCase();
const safeURL=v=>{try{const u=new URL(v);return ['https:','http:'].includes(u.protocol)?u.href:''}catch{return ''}};
const titleKey=v=>str(v).normalize('NFKC').toLowerCase().replace(/[^\p{L}\p{N}]/gu,'');
function base(r={}){return {uid:r.uid||globalThis.crypto.randomUUID(),title:str(r.title),authors:Array.isArray(r.authors)?r.authors.map(str):[],year:str(r.year),journal:str(r.journal),doi:doi(r.doi),pmid:str(r.pmid),pmcid:str(r.pmcid),source:str(r.source),sourceId:str(r.sourceId),abstract:str(r.abstract),types:Array.isArray(r.types)?r.types.map(str):[],freeURLs:Array.isArray(r.freeURLs)?r.freeURLs.map(safeURL).filter(Boolean):[],url:safeURL(r.url),origins:Array.isArray(r.origins)?r.origins.map(str):[],status:['unreviewed','keep','maybe','exclude','read'].includes(r.status)?r.status:'unreviewed',notes:str(r.notes),copyURL:safeURL(r.copyURL),copyFile:str(r.copyFile),hasCopy:!!r.hasCopy,added:r.added||new Date().toISOString()};}
function epmc(r,origin){return base({title:r.title,authors:r.authorList?.author?.map(a=>a.fullName)||[r.authorString].filter(Boolean),year:r.pubYear,journal:r.journalInfo?.journal?.title||r.journalAbbreviation,doi:r.doi,pmid:r.pmid||(r.source==='MED'?r.id:''),pmcid:r.pmcid,source:r.source,sourceId:r.id,abstract:r.abstractText,types:r.pubTypeList?.pubType||[r.pubType||r.citationType].filter(Boolean),freeURLs:[...(r.fullTextUrlList?.fullTextUrl||[]).filter(u=>['OA','F'].includes(u.availabilityCode)||/^(open access|free)$/i.test(u.availability||'')).map(u=>u.url),...(r.pmcid?[`https://pmc.ncbi.nlm.nih.gov/articles/${r.pmcid}/`]:[])],url:r.id&&r.source?`https://europepmc.org/article/${encodeURIComponent(r.source)}/${encodeURIComponent(r.id)}`:'',origins:[origin]});}
function crossref(r,origin){return base({title:r.title?.[0],authors:(r.author||[]).map(a=>[a.family,a.given].filter(Boolean).join(', ')||a.name||''),year:r.published?.['date-parts']?.[0]?.[0]||r.issued?.['date-parts']?.[0]?.[0],journal:r['container-title']?.[0],doi:r.DOI,abstract:r.abstract,types:[r.type].filter(Boolean),url:r.URL,origins:[origin]});}
function same(a,b){
 if(a.doi&&b.doi)return a.doi===b.doi;
 if(a.pmid&&b.pmid)return a.pmid===b.pmid;
 if(a.source&&b.source&&a.source===b.source&&a.sourceId&&a.sourceId===b.sourceId)return true;
 const key=titleKey(a.title);return key.length>=25&&key===titleKey(b.title)&&!!a.year&&a.year===b.year;
}
function mergeInto(records,incoming){const ids=[];let added=0;
 for(const raw of incoming){const n=base(raw);if(!n.title&&!n.doi&&!n.pmid)continue;const old=records.find(r=>same(r,n));
 if(old){for(const k of ['title','year','journal','doi','pmid','pmcid','source','sourceId','abstract','url'])if(!old[k]&&n[k])old[k]=n[k];
 for(const k of ['origins','freeURLs','types'])old[k]=[...new Set([...old[k],...n[k]])];if(!old.authors.length)old.authors=n.authors;
 // A fresh search must never overwrite screening or a user-supplied copy.
 ids.push(old.uid);
 }else{records.push(n);ids.push(n.uid);added++}}
 return {ids:[...new Set(ids)],added};
}
function csv(records){const cols=['title','authors','year','journal','doi','pmid','publication_types','access','free_full_text_urls','status','notes','my_copy_url','my_copy_filename','found_via','record_url'];
 const cell=v=>'"'+str(v).replace(/^[\s]*[=+@-]/,m=>"'"+m).replaceAll('"','""')+'"';
 return '\uFEFF'+[cols,...records.map(r=>[r.title,r.authors.join('; '),r.year,r.journal,r.doi,r.pmid,r.types.join('; '),r.hasCopy?'Copy obtained':r.freeURLs.length?'Free link listed':'Access unresolved',r.freeURLs.join('; '),r.status,r.notes,r.copyURL,r.copyFile,r.origins.join(' | '),r.url])].map(row=>row.map(cell).join(',')).join('\r\n');}
function ris(records){const line=(tag,v)=>v?`${tag}  - ${str(v).replace(/[\r\n]+/g,' ')}\r\n`:'';return records.map(r=>'TY  - GEN\r\n'+line('TI',r.title)+r.authors.map(a=>line('AU',a)).join('')+line('PY',r.year)+line('JO',r.journal)+line('DO',r.doi)+line('AN',r.pmid)+line('UR',r.doi?`https://doi.org/${encodeURIComponent(r.doi)}`:r.url)+line('AB',r.abstract)+line('N1',[r.notes,`Screening: ${r.status}`,`Found via: ${r.origins.join(' | ')}`].filter(Boolean).join('; '))+'ER  - \r\n').join('\r\n');}
const api={doi,safeURL,titleKey,base,epmc,crossref,same,mergeInto,csv,ris};if(typeof module!=='undefined')module.exports=api;else root.PaperCore=api;
})(globalThis);
