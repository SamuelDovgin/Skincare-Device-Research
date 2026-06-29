# Facebook Marketplace Seller Activity Analysis For The $50 Tria Precision

**Purpose:** Analyze the seller/listing behavior around the $50 Tria Laser Removal listing, after no reply for roughly 10 hours, using the extracted CSV and HAR-derived Marketplace data.

**Privacy / data hygiene note:** The HAR and pasted curl text include sensitive browser/session material. This note uses only listing-level Marketplace facts and does not preserve cookies, auth tokens, private headers, exact profile image URLs, or internal request payloads.

---

## 1. Bottom Line

The seller looks **real and reasonably credible**, but the Tria listing is **old and probably stale/low-priority**.

My read:

| Question | Answer |
|---|---|
| Is the seller probably legitimate? | **Yes, likely.** Highly rated Marketplace badge, long-standing Facebook account, 21 sold-history rows, 13 active/in-stock rows in the extracted data. |
| Is the $50 Tria still marked available in the data? | **Yes.** The target PDP object says `IN_STOCK`, live, not sold, messaging enabled. |
| Is the Tria newly listed? | **No.** It was listed March 26, 2026 at 2:50:33 AM CDT, about 90 days before the June 23 capture. |
| Has the seller listed newer items since the Tria? | **Yes.** Four active listings were created May 29, 2026 at 9:49:02 AM CDT. |
| Can the files prove the seller is online now? | **No.** There is no reliable "currently online" field in the extracted seller/listing data. |
| Does no reply after ~10 hours mean dead listing? | **Not necessarily.** More likely casual seller / slow Marketplace checking than scam. |
| Should you bid up? | **No.** The old listing gives negotiation leverage. $40 remains the right offer. |

**Practical read:** this is likely a normal local decluttering seller, not a high-touch reseller. A 10-hour silence is annoying but not conclusive. I would wait until roughly the next active daytime/evening window, then send one light follow-up. Do not send repeated messages.

---

## 2. Files Used And Excluded

| File | Used? | Why |
|---|---:|---|
| `amneh_marketplace_seller_activity_comprehensive.csv` | Yes | Main structured source for listings, status, creation times, prices, ratings, and notes. |
| `marketplacetestjun.har` | Yes | Backing HAR for active/in-stock seller listing details. |
| `marketplacetestjun23triafraxsold.har` | Yes | Backing HAR for sold-history details. |
| `pasted-text.txt` attachment | Yes | Includes prior extraction context and the target PDP detail. |
| `marketplacetestjun23triafrax.har` | Mostly no | Parsed response scan found no seller listing-like objects for this seller/target; likely the unrelated Tria Frax / $100-to-$80 item the user mentioned. |

HAR capture windows, converted from the HAR `startedDateTime` values:

| HAR | Approx capture window |
|---|---|
| `marketplacetestjun.har` | Jun 23, 2026 10:10-10:33 PM CDT |
| `marketplacetestjun23triafrax.har` | Jun 23, 2026 10:54 PM CDT |
| `marketplacetestjun23triafraxsold.har` | Jun 23, 2026 11:17-11:18 PM CDT |

---

## 3. Seller Profile Signals

Extracted seller-level signals:

| Signal | Value | Interpretation |
|---|---|---|
| Display name | Amneh W. Gh | Marketplace display name from listing data. |
| Facebook join time | Oct 24, 2014 | Long-standing account, not a brand-new throwaway. |
| Marketplace badge | Highly rated on Marketplace | Positive trust signal. |
| Seller-only rating | 4.7 / 5 across 10 seller ratings | Good seller-specific signal. |
| Combined buyer/seller rating | 4.9 / 5 across 24 ratings | Good broader Marketplace signal. |
| Location | Orland Park, IL | Consistent across listings. |
| Delivery | In-person/local pickup | Lower shipping-scam risk; means pickup logistics matter. |
| Messaging | Enabled on listings | Buyer can message; no data proving response speed. |

**Trust conclusion:** nothing in the extracted listing data screams scam. This seller looks like a real local Marketplace user with a history of completed sales.

---

## 4. Safe Orland Park / Seller Context

The safe thing to infer is that this is an **Orland Park-area Marketplace seller**, not an identity to investigate outside the transaction.

I did **not** try to deanonymize the seller, find a home address, phone number, workplace, relatives, or non-Marketplace accounts. For a local pickup purchase, the useful facts are Marketplace trust and logistics, not personal background.

What the listing data supports:

| Signal | What it suggests |
|---|---|
| Orland Park, IL location is consistent across listings | The seller is probably operating locally in/near Orland Park rather than using a random one-off location. |
| In-person delivery type across listings | This is a local pickup seller, so arranging a normal public/safe pickup spot is appropriate. |
| Joined Facebook in 2014 | Long-lived account, which reduces throwaway-account concern. |
| Highly rated Marketplace badge | Positive platform-level trust signal. |
| 4.7 seller rating / 10 seller ratings | Enough seller-specific ratings to treat the account as established. |
| 21 sold-history rows in extracted data | Seller has completed Marketplace activity before. |
| Listings are mostly household/clothing/personal items | Pattern looks like decluttering/resale, not an obvious scam inventory pattern. |

What this does **not** prove:

- that the seller is online today
- that she has read your message
- that the exact Tria is still physically available
- that the pickup will be at her home or a public location
- that the device works

**Pickup implication:** if she replies, keep it simple and use normal Marketplace safety. Meet in daylight if possible, bring exact cash, and verify the device powers on/unlocks before handing over money. No need to dig further into the person.

---

## 5. Target Tria Listing Facts

Target listing:

| Field | Value |
|---|---|
| Title | Tria Laser Removal |
| Price | $50 |
| Status | `IN_STOCK` |
| Sold? | False |
| Pending? | False |
| Hidden? | False |
| Messaging enabled? | True |
| Condition | Used - like new |
| Location | Orland Park, IL |
| Listing created | Mar 26, 2026 at 2:50:33 AM CDT |
| Age at Jun 23, 2026 11:30 PM CDT | 89 days, 20 hours, 39 minutes |
| Source note | Target item; listed in same March 26 batch as multiple other seller items; still live/in stock in captured PDP. |

Seller description:

> Tria hair removal, used twice only on the face.
> Has a small scratch as shown in the picture but it is working 100%.
> Has charger and plugs for all outlets types that could be used in any country.
> Purchased originally 2 years ago for $245.

**Interpretation:** the listing is not fresh. It has been sitting for about 3 months. That strongly supports opening at $40 and not feeling pressure to jump to $50 unless the seller responds and proves the device works.

---

## 6. Listing Batch Pattern

The seller appears to post in batches, not one item at a time every day.

### Active listings captured

| Batch time | Count | Titles |
|---|---:|---|
| Mar 26, 2026 2:50:33 AM CDT | 5 | Michael Kors handbag; Men's set; chandelier; White Mountain boot; **Tria Laser Removal** |
| Mar 26, 2026 2:50:34 AM CDT | 4 | Gaming/TV Stand with Storage; Shein shoes; Holder for napkins; Makeup/brushes organizer |
| May 29, 2026 9:49:02 AM CDT | 4 | Dining Chairs; Michael Kors shoes; Clarks Shoes; decorations |

The Tria was part of a **bulk listing session** on March 26. The May 29 batch is important because it proves the seller had Marketplace activity after listing the Tria.

Important nuance: in the extracted data, the May 29 items are **not** marked sold. All four May 29 rows are still `IN_STOCK`, and none of them appears in the sold-history rows. That means May 29 proves later listing activity, but it does **not** prove a completed sale or response/check-in after May 29.

### Online context: why several items can appear at once

Checking Facebook/Meta documentation changed the interpretation slightly: a same-minute batch does not have to mean someone manually typed every listing in that exact minute.

Supported explanations:

| Explanation | Online support | Fit to this seller |
|---|---|---|
| Manual decluttering session | Common Marketplace behavior; the captured titles are household/personal goods. | **Best fit.** The categories are mixed household, shoes, decor, and personal items rather than store inventory. |
| Spreadsheet/CSV bulk upload | Facebook Help says Marketplace can accept a CSV/spreadsheet upload for multiple listings at once. | Possible, but not proven. The account data does not show a business/catalog flag. |
| Commerce Manager catalog/data feed | Meta Commerce docs describe product catalogs and data feeds using spreadsheet/XML/feed uploads for adding products in bulk. | Less likely for this specific seller because the listings look local and personal, not ecommerce catalog inventory. |
| Marketplace partner/API batch upload | Meta developer docs describe batch item upload/update/delete endpoints for Marketplace partners. | Unlikely here. Nothing in the extracted fields suggests a partner integration. |
| Delete/relist or renew-style refresh | Sellers sometimes recreate old listings to refresh visibility, but the provided data does not show edit/relist history. | Possible for some Marketplace sellers, but not supported by these rows. |

Source links:

- Facebook Help Center: [Use a spreadsheet for multiple listings on Facebook Marketplace](https://www.facebook.com/help/1943158472539049)
- Meta Business Help Center: [Ways to add products in your catalog](https://www.facebook.com/business/help/384041892421495)
- Meta for Developers: [Catalog reference](https://developers.facebook.com/documentation/ads-commerce/catalog/reference/)
- Meta for Developers: [Marketplace Partner Item API](https://developers.facebook.com/docs/marketplace/partnerships/itemAPI/)

**Updated interpretation:** the identical or near-identical creation times are reliable evidence of a batch listing event, but not reliable evidence of live responsiveness. The strongest seller-specific read remains: this looks like a local person posting a group of household items in one sitting, with bulk-upload tooling as a plausible but unproven alternative.

### Timeline plot

Each `#` is one listing created at the exact batch timestamp in the extracted data.

```text
2026-03-21 14:07  #     sold-history item: Outdoor umbrella stand
2026-03-26 02:50  ##### target batch includes Tria
2026-03-26 02:50  ####  same minute, more active listings
2026-05-29 09:49  ####  newer active listings
```

**Behavioral read:** she may batch-post household/clothing items when decluttering. She is not obviously managing Marketplace every day. A May 29 item being sold would have been stronger evidence of recent active transaction management, but this capture does not show that.

---

## 7. Sold-History Pattern

The CSV includes 21 sold-history rows from 2024-2026. The rows show sale history exists, but the HAR data does **not** expose reliable sold timestamps.

Important caveat:

- `creation_time` is the listing creation time, not a confirmed sold time.
- The extracted source notes repeatedly say no `sold_at`, `sold_time`, or `marked_sold_at` field was found.
- Sold-list row order may reflect the displayed sold list order, but it is not enough to prove exact sale dates.
- A sanitized JSON copy of the useful fields is saved at [marketplace_seller_activity_sanitized.json](marketplace_seller_activity_sanitized.json). It preserves listing creation times, status, sold flags, display-order rank, price fields, and source trace notes, while omitting cookies, auth tokens, exact coordinates, profile image URLs, and raw GraphQL payloads.

Direct answer to "does Facebook give any info on when stuff was sold?" from these captures:

| Possible field | Found? | Meaning |
|---|---:|---|
| `is_sold` | Yes | Confirms whether the listing is currently sold/sold out. |
| `renderable_listing_status` | Yes | Shows `SOLD`, `SOLD_OUT`, or `IN_STOCK`. |
| `creation_time` | Yes | Listing creation time only. Not sale time. |
| `sold_at` / `sold_time` / `marked_sold_at` | No | No explicit sold timestamp appeared in the extracted rows. |
| `sold_har_display_rank` | Yes for sold-history rows | Display/order clue only; not a timestamp. |

Recent sold-history rows by listing creation time:

| Listing created | Sold-history item | Price |
|---|---|---:|
| Mar 21, 2026 | Outdoor umbrella stand | $15 |
| Jan 10, 2026 | Safety Cabinets Locks | $20 |
| Dec 30, 2025 | Michael Kors M shaped crossbody | $40 |
| Nov 2, 2025 | Gray kids Chairs - Set of 2 | $20 |
| Nov 2, 2025 | Basket Display Stand - Set of 2 | $80 |
| Nov 2, 2025 | Gucci Bracelets | $100 |

**Behavioral read:** she has sold items historically and across many categories. This supports legitimacy, but it does not tell us how quickly she replies.

---

## 8. Description And Seller Style Pattern

The seller's listing text has a pattern:

- Often describes items as gently used, used a few times, or like new.
- Often anchors to original purchase price or store source.
- Discloses visible flaws in several descriptions.
- Uses practical pickup/local language.

Examples from extracted descriptions:

| Listing | Pattern |
|---|---|
| Tria Laser Removal | "used twice", disclosed scratch, original purchase price. |
| Michael Kors handbag | "Excellent condition", original store/purchase price anchor. |
| TV stand | Disclosed small scratches and missing handle to be installed before pickup. |
| Oster blender | Disclosed small crack without leak and pickup-only wording. |
| White Mountain boot | "Used twice" and no scratches/fading. |

**Interpretation:** the Tria description style fits her broader seller pattern. The scratch disclosure is a good sign. The repeated "used twice" style should be treated as plausible but not independently verified.

---

## 9. What The Data Cannot Prove

The files do **not** prove:

- whether she is online right now
- whether she saw your message
- whether she ignored you
- whether the Tria is physically still in her possession
- whether there is another buyer ahead of you
- whether the device battery works
- whether the price was ever reduced

For price reduction history specifically:

| Field | Result |
|---|---|
| Current Tria price | $50 |
| Strikethrough price | Empty |
| Discount text | Not surfaced for target listing |
| Marketplace bump info | Empty |
| Price reduction timestamp | Not found |

**Conclusion:** no evidence of a Tria price drop in the provided fields. The March 26 creation time is reliable; any price-change history is not available from these files.

---

## 10. Prediction: Is She Likely Still Selling Properly?

My prediction, from strongest to weakest:

| Claim | Confidence | Reason |
|---|---:|---|
| The seller is a real Marketplace seller | High | Ratings, badge, old account, sold history, active listings. |
| The Tria listing was live/in stock at capture time | High | Target PDP says IN_STOCK, not sold, not pending. |
| The seller listed newer items after posting the Tria | High | May 29 active batch exists, after Mar 26 Tria listing. |
| The seller is currently active enough to reply eventually | Medium | Newer listings and ratings help; May 29 items are not marked sold, so this is not proof of recent completed sales. |
| The seller is online right now | Unknown | No reliable current-online field in extracted data. |
| The seller will accept $40 | Medium-low to medium | Old listing gives leverage, but seller may be slow/firm. |
| The item is definitely still physically available | Medium | Facebook says in stock, but stale listings can be forgotten. |

**Overall:** not a dead/scammy listing, but definitely an old one. The right move is patient, casual follow-up rather than chasing.

---

## 11. Messaging Strategy

You already sent:

> Hello is this still available? If so would you take $40 cash if I picked it up today

If that message was sent at **12:09 PM**, I would wait roughly 24 hours before following up. If "today" was June 23, 2026, the follow-up window would be **June 24 after about 12-2 PM**, or early evening if you want to catch someone after work.

After roughly 10 hours, I would **not** send another message immediately unless you know she has seen it and you need it tonight.

Best follow-up:

> Hi just checking on this. I can pick it up today if $40 works

Softer version:

> Hi just checking if this is still available. I can pick it up today if that works

Version that keeps the $40 clear but not pushy:

> Hi just wanted to follow up. I'm still interested and can do $40 cash if I pick it up today

If you want to keep $50 possible later:

> Hi just checking if this is still available. I can pick up today and can do $40, or $50 if I can quickly confirm it powers on and holds charge

If no response after 48 hours:

- assume the listing may be stale or low-priority
- do not raise your offer just to get attention
- keep watching for a reply, but move on mentally

---

## 12. Buying Implications For The Tria

Because the item is old but still live:

| Factor | Negotiation effect |
|---|---|
| 90-day-old listing | Strong support for $40 offer |
| Highly rated seller | Makes pickup less concerning |
| No reply for ~10 hours | Mild negative, not decisive |
| May 29 newer listings | Seller not abandoned |
| In-stock status | Good, but stale-listing risk remains |
| No price-drop evidence | Do not assume $50 was already reduced |
| No exact online/seen field | Cannot infer current attention |

**Final action:** wait. If she replies, stay at $40 unless she insists. If she insists on $50, only pay it after a function check: turns on unplugged, unlocks, cycles levels, fires, and has a clean treatment window.

---

## 13. Source Notes

Structured source:

- `~/Downloads/amneh_marketplace_seller_activity_comprehensive.csv`

Sanitized repo artifact:

- [marketplace_seller_activity_sanitized.json](marketplace_seller_activity_sanitized.json) - safe JSON snapshot of the relevant seller/listing data, including active listings, sold-history listings, batch summaries, target Tria fields, and a sold-timestamp field audit.

HAR sources inspected:

- `~/Downloads/marketplacetestjun.har`
- `~/Downloads/marketplacetestjun23triafraxsold.har`
- `~/Downloads/marketplacetestjun23triafrax.har` (ignored for conclusions; no relevant seller/listing objects parsed)

Attachment context:

- `~/.codex/attachments/ae16e79f-df5b-49f0-8c1d-1c3e6f510ea8/pasted-text.txt`

Local Tria valuation context:

- [09_tria_precision_marketplace_assessment.md](09_tria_precision_marketplace_assessment.md)
- [10_used_tria_value_and_wear_pricing.md](10_used_tria_value_and_wear_pricing.md)
