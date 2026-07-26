# Tria Precision: Low Pulses Worked, High Pulses Collapsed, Then the Unit Went Dead

**Compiled:** 2026-07-18; updated 2026-07-20  
**Scope:** A case-specific failure analysis and warranty-return plan for a Tria Laser Precision that worked after a battery replacement, began shutting off exactly when it tried to deliver a treatment pulse, temporarily appeared completely unresponsive, and now occasionally boots again after resting without being charged but dies on the first Low pulse. This is technical research orientation, not a remote electrical diagnosis. Do not open or modify a lithium-battery laser while a repair warranty is active.

## 0. Bottom line

The most likely root cause remains **a failure in the battery/charging/current-delivery path**, not the laser diode itself. The fact that the unit reportedly completed about three normal treatment sessions—including more than 100 successful High pulses—during the first week after it was received back shows that the replacement system and laser path initially handled the highest treatment load. It now occasionally recovers enough to boot **without any new charging**, powers the fan and skin sensor, and then dies on the first attempted Low pulse.

That rest-and-retry behavior is classic for a source that can supply low current at its recovered resting voltage but collapses when the laser load begins. Lithium-ion voltage rises again after load removal because the instantaneous resistance drop disappears and slower electrochemical polarization relaxes; this does not restore the charge removed from the cell. [[5]](https://www.mdpi.com/2313-0105/8/8/77) A battery protector can also be designed to recover after a timer expires or after load removal, although the exact protection circuit inside this Precision has not been identified. [[6]](https://www.ti.com/lit/ds/symlink/bq77905.pdf)

The new evidence particularly supports three possibilities:

1. the new battery is largely discharged because the charging board never properly replenished it;
2. the replacement cell, its protection components, or a repaired connection has developed excessive resistance;
3. a protection device is disconnecting the battery when pulse current begins and later resetting.

A laser-driver or diode fault can still create an abnormal load only when firing is commanded, so it is not impossible. But an actual shorted laser diode is now a distinctly lower-probability explanation than the battery/charge/current path.

The timing is highly diagnostic:

- the device charges and powers its controls and fan;
- it unlocks normally;
- before the failure began, it reportedly completed about three full treatment sessions, including more than 100 successful pulses on High, and appeared completely functional for roughly one week after it was received back on July 11;
- it completed roughly 2–3 pulses at the lowest energy setting;
- on two attempts at the highest setting, it did not complete even the first pulse and appeared to begin firing for only about 0.1 second before shutting off;
- behavior at the middle setting is not recalled clearly enough to classify;
- it initially remained dead until roughly 30 minutes on the charger let it boot and repeat the same failure;
- after being left on the charger overnight, it initially gave no power-on feedback at all;
- as of July 20, it occasionally boots again after resting without being charged, powers the fan and skin sensor, and then shuts off on the first attempted pulse even at Low;
- the failure appeared approximately one week after the repaired device was received back.

That sequence points to a **later-developing load-dependent power collapse**, not a skin-sensor or unlock problem. The three initially successful sessions and 100+ High pulses show that the repaired device could operate normally for a meaningful period; they do not prove that every connection, charging function, or cell characteristic remained healthy. Completing several Low pulses during the first failure stage proved that contact detection, the firing command, and at least a full low-energy treatment cycle still worked. Failing twice before completing one High pulse showed that the fault first became visible under the largest demand. Now failing on the first Low pulse shows that the available current margin has deteriorated further.

This should be handled promptly as a **post-repair warranty problem**. Do not keep repeating pulse tests simply because it occasionally boots; the new Low-pulse shutdown has already supplied the useful diagnostic information. Unplug it, do not open it, and report the progression to the repairer. If it becomes hot, swells, leaks, hisses, or develops an unusual odor, keep away from it and combustible material and follow local emergency guidance. The repairer should first inspect the charging, battery, protection, and current path under load.

## 1. What was observed

| Stage | Observed behavior | What it tells us |
|---|---|---|
| First week after the July 11 return | Roughly three complete treatment sessions, including more than 100 High pulses, with apparently normal operation | The battery and laser path initially supported the maximum setting; a later-developing fault fits better than total incompatibility from day one |
| Earlier charging behavior | After about 30 minutes on the charger following a shutdown, it could turn on again | Added charge or a charger-mediated reset temporarily restored booting, but not pulse capability |
| Earlier startup | Indicator lights and fan operated | Low-to-moderate loads were initially available |
| Unlock | Skin-tone unlock completes normally | The skin sensor and basic control logic are functioning |
| Lowest setting | Roughly 2–3 treatment pulses completed | Sensor, unlock, firing command, diode path, and low-energy pulse cycle were functional at that time |
| Highest setting | On two attempts, the device did not complete even one High pulse | Failure has a strong energy/load dependency |
| Brief High-pulse onset | The failed High attempts appeared to begin firing for about 0.1 second before shutdown | The laser-drive phase began; power then failed under the higher demand |
| Middle setting | Behavior is not recalled with enough confidence | Do not claim that every level failed |
| Immediately afterward | Power button does nothing | Supply voltage likely fell below an operating threshold, or a protection/control state disconnected the load |
| State immediately after overnight charging | No power-on feedback; the earlier 30-minute charger recovery did not occur | At that point the device lacked enough usable power even for startup |
| Intermittent state as of July 20 | After resting without any charging, it occasionally powers on, runs the fan, and completes the skin-sensor check; the first Low pulse then shuts it off | Strong evidence for resting-voltage rebound, a protection reset, or an intermittent/high-resistance current path; startup alone does not show that the battery can support pulse current |

The Precision manual says it automatically turns off when its battery is low, may require a mid-treatment charge on large areas or high settings, and should be charged for at least two hours when low. It also says the unit cannot operate while connected to the charger. [[1]](Tria_Precision_IFU_HRLp.pdf) Therefore, the normal consumer test is necessarily performed unplugged—but a healthy, charged replacement should not die at the first attempted pulse.

One detail remains important to report precisely: whether "no feedback whatsoever" means **no response after unplugging and pressing Power**, or also **no charging lights/fan while the original charger is connected**. The first proves persistent no-power operation; the second would additionally strengthen the case for an open battery connection, charger/charge-input failure, temperature-sense interruption, or a deeply failed/disconnected cell.

## 2. Why the first pulse is the key clue

Tria's battery-powered-laser patent describes a topology in which the battery powers the laser diode through high-current switching rather than merely running a low-power control board. In one disclosed embodiment, a single 18650-type lithium-manganese cell with 4.2 V open-circuit charged voltage and 0.016 ohm internal series resistance can generate 75 A through the laser; the patent separately describes a diode that can withstand 80 A or more in sub-second pulses. [[2]](https://patents.google.com/patent/US20140214136A1/en)

Those numbers are a **patent embodiment, not a measurement of this individual Precision**, so they should not be converted into a replacement-cell shopping specification. They do establish the important architecture: pulse performance is unusually sensitive to the total series resistance of the cell, tabs, wiring, joints, switches, and diode path.

The basic relationship is:

`loaded voltage = open-circuit voltage - current × total series resistance`

When current rises sharply, a cell with elevated internal resistance—or a poor joint adding only a small amount of resistance—can show acceptable voltage at rest but collapse below the device's operating cutoff under load. A resting-voltage check can therefore miss the fault.

### What successful Low pulses and failed High pulses add

The pulse count and approximately 0.1-second duration are user recollections, not instrumented measurements, but the setting contrast is still highly useful. Completing 2–3 Low pulses means the device was capable of a full treatment cycle under lower demand. On two High attempts, the laser-drive stage apparently began but could not finish even one treatment pulse.

Tria does not publicly disclose the exact current waveform, PWM duty cycle, or pulse-duration mapping for each Precision level. The highest level nevertheless represents the highest delivered optical energy setting, so the cleanest inference is that the electrical/thermal demand crossed a failure threshold at High. That makes these explanations less likely:

- a skin-tone sensor that never unlocked;
- failure caused only by poor contact with the treatment window;
- a software state that never commanded a pulse;
- a completely open battery connection during the earlier Low-pulse phase.

It materially strengthens a supply-capability explanation because the unit completed Low pulses but collapsed during High. It does not by itself separate a failing/high-resistance cell from a resistive connection, charging problem, or abnormal High-setting laser-driver load. The later totally dead state means the underlying fault then progressed.

### What three successful sessions add

About three completed sessions and more than 100 successful High pulses over the preceding week are fully compatible with the later diagnosis, but they make the timeline more specific. They strongly weaken the narrow theories that the replacement was completely incapable of supplying pulse current from installation or that the diode path was already shorted when the unit returned. They strengthen **failure after initially normal operation**: a battery that was not subsequently recharged, a defective cell that deteriorated, a marginal joint or tab that worsened through heat/mechanical cycling, or a later electronics fault.

This history also modestly raises the possibility of an unrelated laser-driver or main-board fault, because a device can develop a new electronics fault after a successful repair. It does not raise that possibility above the battery/current path: the failure remained strongly load-dependent, progressed to total loss of power, and appeared shortly after that path was serviced.

The reported 100+ High pulses are particularly strong evidence that the installed system initially handled High demand. They are not a measured battery-cycle test and do not prove that the battery was actually recharged between sessions. If the replacement cell arrived charged while a pre-existing charging fault remained, the device could work normally until that initial charge was consumed.

### What the later no-charge recovery changes

The overnight charge initially failed to restore startup, but the unit now occasionally boots after resting **without** another charge. That changes the interpretation:

1. **Voltage rebound becomes a leading immediate mechanism.** A depleted or high-resistance lithium-ion cell can recover enough terminal voltage at rest to boot a low-current control board without regaining meaningful charge. [[5]](https://www.mdpi.com/2313-0105/8/8/77)
2. **Protection reset becomes more plausible.** Some battery-protection designs restore their discharge path after a timer or load-removal condition; this is generic mechanism evidence, not proof of the circuit Tria used. [[6]](https://www.ti.com/lit/ds/symlink/bq77905.pdf)
3. **A hard-open connection becomes less likely than an intermittent or resistive one.** The controls repeatedly receive power, but the path cannot support a laser pulse.
4. **A charging-board fault remains highly plausible.** The lights and logic can operate even if the cell is not being properly charged. A new cell may have supplied the first week's 100+ High pulses from its installation charge and then gradually become depleted.
5. **A hard laser-diode short moves down.** It can still cause collapse when the driver turns on, but the whole pattern is explained more naturally by inadequate supply voltage/current.

## 3. Correcting the battery-chemistry confusion

Earlier troubleshooting notes mixed evidence from the larger **Tria 4X** with the **Tria Precision**. That produced a recommendation for a 3.2 V LiFePO4 cell. It should not be used for this Precision case.

The repair listing photograph identifies the Precision pack as **TB P#11777B-02**. [[3]](https://www.ebay.com/itm/255665106179) A model-specific battery-recell service lists that exact part number and Precision model 11777C-03 as **3.6 V nominal, 1950 mAh, lithium-ion**, and offers higher-capacity lithium-ion recells. [[4]](https://www.batt.co.jp/products/detail/6530) Tria's patent likewise includes a single 18650-type lithium-manganese example with 4.2 V fully charged. [[2]](https://patents.google.com/patent/US20140214136A1/en)

The evidence supports this practical conclusion:

> **Do not recommend a generic 3.2 V LiFePO4 replacement for the Precision.** Ask the repairer for the exact manufacturer and model of the cell actually installed, its chemistry, nominal and full-charge voltage, capacity, pulse/continuous-current rating, and measured internal resistance. The publicly available sources do not disclose enough to nominate a safe substitute cell by model number.

Higher capacity is not automatically better. A 2600-3500 mAh energy-oriented cell can provide longer runtime yet perform worse in this application if its internal resistance or pulse-current capability is inferior to the original high-power cell.

## 4. Ranked failure analysis

These rankings are conditional inferences based on timing and symptoms; the device has not been instrumented. A rough working split for the **primary root cause** is:

| Primary root-cause category | Rough likelihood | Why |
|---|---:|---|
| Battery cell, repaired connection, pack protection, or temperature-sense path | **45%** | Low-current boot followed by immediate pulse collapse and recovery after rest are a strong supply-path pattern |
| Charging board or charge-input/monitoring fault | **40%** | A charged replacement could supply 100+ High pulses, then become depleted if the original charging fault was never corrected |
| Laser-driver/switching electronics | **10%** | Can create an excessive load only when a pulse is commanded, but does not explain the complete timeline as economically |
| Laser diode itself shorting/failing | **5%** | Possible later abrupt failure, but less consistent than supply-path explanations and not supported by a diode-specific measurement |

These percentages are judgment estimates, not failure-rate data, and should be treated as approximately plus or minus 10 percentage points. The useful distinction is that the charging/battery/current path collectively accounts for roughly **85%** of the working hypothesis; the diode itself is a minority possibility.

### 1. Replacement cell, repaired connection, or pack-protection/sense fault — high likelihood

This category remains marginally the best explanation for the complete timeline. The cell reportedly supported about three full sessions and more than 100 High pulses, then later supported the fan, logic, and 2–3 completed Low pulses but sagged before completing a High pulse twice. It now occasionally recovers enough to boot after resting, then collapses on the first Low pulse. That progression is compatible with a cell whose internal resistance or usable capacity worsened, an intermittent/high-resistance repair connection, or pack-protection/sense behavior.

This category includes several root causes that cannot be separated remotely:

- a new but defective cell with unusually high internal resistance;
- a capacity-focused cell with inadequate long-term margin, although three initially successful sessions make total from-day-one current incapability less likely;
- heat or mechanical damage during installation;
- a cell that the charge circuit is terminating early because its voltage/temperature sensing is wrong;
- a replacement that was initially marginal and rapidly revealed the problem during normal sessions.

If the Precision pack is the single-cell design indicated by the model-specific 3.6 V pack data and Tria patent example, this is **not best described as one dead cell in a multi-cell series pack**. It is more likely one cell whose loaded voltage is unacceptable even though its resting voltage appears plausible.

### 2. Resistive or open installation fault at a tab, weld, solder joint, wire, or connector — medium-high likelihood, raised

A marginal connection adds series resistance exactly where this design is most sensitive to it. It can initially pass enough current for approximately three normal sessions, then worsen through thermal or mechanical cycling, drop too much voltage during High, and eventually become an effectively open path. The initial successful period followed by a load-dependent failure and then persistent no-power state makes this explanation more—not less—coherent.

The repairer should inspect and measure the entire current path rather than merely reseating the pack.

### 3. Charging-board or charge-input fault — high likelihood, approximately tied with the battery/current path

The device may have displayed or behaved as though it charged while the new cell was actually left at a low state of charge. The history before the battery service matters here: if the old battery appeared charged while plugged in but the device died as soon as it was unplugged, replacing only the battery could temporarily mask a pre-existing charging fault. The new cell may have arrived with enough charge for the first week's 100+ High pulses and then never been properly replenished. A disturbed thermistor/sense connection, failed charging IC or input path, or incorrect charge termination could create the same result.

This is what Tony likely means by "the charging board": the circuitry that accepts adapter power, controls current/voltage into the cell, and monitors charge conditions can fail even while separate control electronics, indicator lights, the fan, and skin sensor still work. The overnight charger connection does not prove that energy reached the cell.

### 4. Protection cutoff — plausible immediate mechanism, unproven root cause

An undervoltage or overcurrent protector may disconnect the load when the pulse is requested. The intermittent return after resting raises this immediate mechanism because generic protection ICs can recover after a timer or load-removal condition. [[6]](https://www.ti.com/lit/ds/symlink/bq77905.pdf) The public Precision material does not identify the installed protection circuit or its reset behavior, so this remains a mechanism rather than a remotely proven root cause. Even if protection is what switches the unit off, the cause of the trip may still be a depleted/weak cell, excess connection resistance, or an abnormal laser-driver load.

### 5. Laser-drive board fault — low but non-zero likelihood

A shorted or abnormal drive component could demand excessive current whenever a pulse is commanded and cause the same shutdown. More than 100 earlier High pulses rule out a driver that was incapable from the start, but not a component that later failed abruptly. It remains below the battery/charge path because the unit now boots after rest and collapses under even the lowest laser demand. If a known-good, fully charged, correct high-current cell and verified connections still fail, board-level current and switching waveforms become the next test.

### 6. Laser diode itself failing or shorting — low likelihood

A diode can fail abruptly after previously working, so 100 successful High pulses do not make it impossible. A diode or its immediate output path that becomes abnormally low resistance could pull the supply down only when the driver enables it. However, "the diode is shorting and depleting the battery" is too specific for the observed evidence. In the Tria patent architecture, switching electronics gate the high-current path; a shorted diode would not necessarily drain the battery continuously while no pulse is being commanded. [[2]](https://patents.google.com/patent/US20140214136A1/en) Loaded battery voltage and laser-current measurements are needed before assigning the fault to the diode rather than the cell, connection, protection, charger, or driver.

### 7. External charger alone — lower likelihood than the internal charging path

A failed charger or charge input could explain why the unit did not recover overnight. It does not explain as cleanly why the device previously shut down precisely after the laser pulse began, so it is not a satisfying explanation for the whole timeline. The repairer should test the original charger output and the device's charge input as part of the battery system. Do not experiment with an unverified substitute charger.

## 5. Did using it until automatic shutdown cause this?

Probably not in one week. The official manual explicitly anticipates the battery becoming low, the device automatically turning off, and users recharging mid-treatment when necessary. [[1]](Tria_Precision_IFU_HRLp.pdf) Repeatedly exhausting a lithium cell is not ideal for long-term cycle life, but ordinary use to the device's own cutoff should not make a correctly specified, healthy replacement unable to deliver even one pulse after approximately one week.

That usage may have **exposed** a marginal cell sooner. It is not a convincing basis for treating the failure as normal wear or user-caused damage.

## 6. What to document before sending it back

Do not keep recreating the pulse failure. If it naturally powers on again after resting, record the fan, indicators, and successful skin-sensor check, but another treatment-pulse attempt is not needed. Do not open, strike, squeeze, or repeatedly cycle the charger.

1. State that it was left on the original charger overnight.
2. Show whether connecting the original charger produces any charging lights, fan activity, or other feedback.
3. Document that it now occasionally powers on after resting without being charged, including normal fan and sensor operation.
4. State that it completed about three normal sessions and more than 100 High pulses during the first week after it was received back on July 11.
5. State that after the fault began it still powered on, unlocked, and completed about 2–3 pulses at Low.
6. State that on two attempts at High it did not complete even one pulse and appeared to begin firing for about 0.1 second before dying.
7. Preserve any earlier video that captured the pulse-triggered shutdown; do not reproduce it now.
8. State the repair return date, when each stage began, that the overnight charge initially produced no response, and that later startup sometimes returns after rest without charging.

Keep the order record, original tracking, repair messages, and the seller's 30-day-warranty representation. Do not open the device or disturb the repairer's seals. Ask whether the charger should be included in the return; the original transaction requested it for diagnosis.

## 7. What the repairer should verify

A useful warranty inspection should include:

- exact replacement-cell manufacturer and model—not only voltage and mAh;
- chemistry, nominal voltage, full-charge voltage, capacity, continuous/pulse-current rating, and cell internal resistance;
- battery terminal voltage at rest, at startup, and during an attempted treatment pulse, preferably captured fast enough to see a transient drop;
- voltage drop across tabs, joints, wiring, and connectors during the same event;
- integrity of any temperature-sense lead and protection/monitoring components that were reused;
- charger output and actual end-of-charge cell voltage;
- continuity and voltage drop through every recently disturbed tab, weld, solder joint, wire, and connector;
- if the battery path passes, laser-driver current and switching behavior;
- a meaningful post-repair pulse/session test, not merely confirmation that the device powers on and charges.

## 8. Message options: start casual, add detail only when useful

The first message does not need the entire electrical theory. Start with the **standard version** unless the repairer already asked for diagnostic detail. Add the technical follow-up only if Tony asks what you think is happening, says the unit merely needs charging, or reports that it passed a basic power-on test.

| Situation | Best message |
|---|---|
| You are attaching a clear video and want the quickest possible note | Very short |
| First warranty contact in the eBay thread | **Standard — recommended** |
| You want all symptoms documented in the first contact | Detailed |
| Tony asks what you think the fault is | Technical follow-up |
| Tony says it charges or powers on normally | Load-test follow-up |
| Tony agrees to inspect it but does not mention shipping | Shipping follow-up |
| You already sent the earlier symptom message | New-condition update |
| The device later starts intermittently without charging | **July 20 diagnostic update** |

### Option A — very short

> Hi Tony, quick follow-up on my Tria Precision battery replacement. I received it back on July 11, and it worked normally for about a week and completed around three sessions. It then managed 2–3 pulses on Low, but on two attempts at High it shut off before completing even one pulse. I left it on the charger overnight, but now it is completely unresponsive. Since this is within the 30-day warranty, can you please let me know how to send it back? Order: 05-14837-05847. Thanks, Samuel

**Use this when:** the video clearly shows the full sequence, or you want to open the conversation without overwhelming him.

### Option B — standard and casual (recommended first message)

> Hi Tony,
>
> I wanted to follow up about the battery replacement on my Tria Precision. I received it back on July 11, and it worked completely normally for about a week and completed around three full treatment sessions, but then it developed a shutdown problem.
>
> At first it would charge, turn on, unlock, and run the fan normally. It managed about 2–3 completed pulses on the lowest setting. However, on two attempts at the highest setting it shut off before completing even one pulse; it seemed to begin firing for only a fraction of a second before dying. It initially became usable again after around 30 minutes on the charger.
>
> I then left it on the charger overnight, but now it gives me no power-on response at all. The earlier charger recovery is no longer working, and it appears to be back in the same completely nonworking condition it was in before the battery service.
>
> Since this started so soon after the battery replacement and is still within the 30-day warranty, could you please take another look at it? Please let me know the return process, whether you would like the charger included again, and whether you can provide a return label.
>
> I can send a video of its current no-power state and explain the earlier pulse-shutdown sequence if that would help.
>
> Order number: 05-14837-05847
>
> Thanks,
> Samuel

**Use this when:** making the first warranty contact. It documents the important pattern without presenting an unconfirmed diagnosis as fact.

### Option C — detailed but still conversational

> Hi Tony,
>
> I am following up about my Tria Precision battery replacement. I received it back on July 11, and it worked completely normally for about a week and completed around three full treatment sessions. It then developed a consistent shutdown problem and has now become completely unresponsive.
>
> During the first stage, the device charged, powered on, unlocked, and ran the fan. It completed about 2–3 pulses on the lowest setting. However, on two attempts at the highest setting it failed before completing even one pulse. It appeared to begin the High pulse for roughly a fraction of a second before the power collapsed. The power button did nothing immediately afterward, although around 30 minutes on the charger initially let it turn on again.
>
> I left it on the charger overnight, but now it gives no power-on feedback at all and the earlier recovery no longer happens. It appears to be back in the same nonworking condition it was in before the battery replacement.
>
> My guess is that something in the new battery, its connection, or the charging path first failed under the heavier laser load and has now progressed, although I understand you would need to test it to know for sure. Since the problem appeared shortly after the repair and is within the 30-day warranty, could you please inspect and correct it under the warranty?
>
> Please send me the return instructions and let me know whether to include the charger. Because the failure occurred so soon after the repair, would you be able to provide a prepaid return label? I can send a video showing the current no-power condition and describe the earlier pulse-triggered shutdown.
>
> Order number: 05-14837-05847
>
> Thanks,
> Samuel

**Use this when:** you want the full symptom history in the first message but still want to sound collaborative rather than accusatory.

### Option D — short update if the earlier message was already sent

> Hi Tony, one important update to my last message: I received it back on July 11, and before this problem began it worked normally for about a week and completed around three full treatment sessions. After the problem started, it still completed about 2–3 pulses on the lowest setting. On two attempts at the highest setting, it did not complete even one pulse and seemed to shut off a fraction of a second after starting. I then left it on the charger overnight, and now it gives no response at all. The earlier 30-minute charger recovery has stopped working. I wanted to add the complete timeline because it may help with the diagnosis.

### Optional follow-up 1 — if Tony asks what you think is wrong

> I cannot know for certain without measurements, but completing a few Low pulses and then failing twice before completing one High pulse makes me wonder whether the replacement cell is dropping voltage when the energy demand increases, or whether there is extra resistance at a battery tab, joint, wire, or connector. A protection cutoff might be what actually shuts it down, although that would not necessarily be the underlying cause. It now occasionally boots after resting without charging, but the first Low pulse immediately shuts it off.

### July 20 diagnostic update — recommended now

> One more update that may help with the diagnosis: every once in a while, after sitting without being charged, the Tria powers on again and the fan and skin sensor work normally. But the first pulse on even the lowest setting immediately shuts it off. Before this problem began, it had completed more than 100 pulses on the highest setting without an issue. Could you please check the battery voltage and connections under load, as well as whether the charging board is actually charging the cell? Thanks.

### Optional follow-up 2 — if he says it charges or passes a power-on test

> Thank you. The issue may not show up from checking resting voltage or only confirming that it turns on: it now occasionally boots and runs the fan and sensor, but the first Low pulse immediately shuts it off. Could you please check the cell and connections under an appropriate controlled load, along with whether the charging and temperature-sensing path is actually charging the cell? If it is repaired, it would be helpful to verify multiple pulses at both Low and High before it is returned.

### Optional follow-up 3 — if he is willing to disclose the installed cell

> Also, just for my records, could you tell me the exact manufacturer and model of the replacement cell you installed? If available, I would appreciate the chemistry, nominal voltage, capacity, pulse or continuous-current rating, and whether the original protection or temperature-sensing parts were reused.

This cell-spec request is useful, but it is optional. Do not let it distract from the main warranty request or make the first message sound like a parts dispute.

### Optional follow-up 4 — if shipping is not addressed

> Thanks for taking another look at it. Since the problem started shortly after the battery replacement and is still within the repair warranty, would you be able to send a prepaid return label? Also, should I include the charger again?

### Optional follow-up 5 — if he suggests only charging or resetting it

> I already left it on the charger overnight; at first it gave no response afterward. It now occasionally powers on after resting without charging, but the first pulse on Low immediately shuts it off. I would like to send it back under the repair warranty.

## 9. Response and shipping strategy

- Send the standard casual message first. Add the technical or cell-spec follow-ups only if the reply makes them useful.
- First ask the repairer to cover the return label, warranty correction, and shipment back.
- Do not offer another repair fee or volunteer to pay both directions before the repairer responds.
- If a prepaid label is refused, a reasonable compromise is paying outbound shipping while the repairer covers diagnosis/correction and return shipping.
- Obtain the return address and packing instructions in the eBay message thread; do not rely on an old address copied from an earlier message.
- Ship the lithium-battery device only by a carrier/service that accepts it, package it against accidental activation and damage, and retain the acceptance receipt and tracking.

## Evidence gaps

- No loaded-voltage trace, cell internal-resistance measurement, or charger end-voltage measurement is available.
- The exact replacement-cell manufacturer/model and installation method are unknown.
- The approximately three successful sessions and 100+ High pulses are user-reported; their exact timing, treatment area, pulse count, and recharge pattern were not recorded.
- The remembered 2–3 Low pulses and approximately 0.1-second High-pulse starts were not instrumented or video-timed; they should be reported as recollection rather than exact measurement.
- Behavior at the middle setting is not recalled clearly enough to classify.
- The intermittent no-charge startup has not been paired with a resting-voltage or state-of-charge measurement; it is compatible with voltage relaxation, protection reset, or an intermittent connection, but does not select among them.
- It remains unclear whether the charger ever restored meaningful runtime after the repair or whether the device used primarily the replacement cell's installation charge. That fact would materially change the relative weighting of charging-board versus cell/connection failure.
- The eBay listing shows the original Precision pack but does not disclose the cell installed by this repairer. [[3]](https://www.ebay.com/itm/255665106179)
- The Tria patent describes possible embodiments; it does not prove the exact cell or peak current used in this individual device. [[2]](https://patents.google.com/patent/US20140214136A1/en)
- The earlier 30-minute charger recovery was consistent with both added charge and a charger-mediated reset. The later recovery after rest without charging is consistent with voltage relaxation, protection reset, or an intermittent connection; neither observation distinguishes the root cause without measurement.
- The 30-day warranty term comes from the owner's order record; the currently accessible public listing title says "best warranty" but does not expose the duration in its description. [[3]](https://www.ebay.com/itm/255665106179)

## Sources

1. Tria Beauty. [Tria Laser Precision Instructions for Use](Tria_Precision_IFU_HRLp.pdf). Local primary manual; supports the charge procedure, automatic low-battery shutdown, mid-treatment recharging, charger-only operation limits, and repair warning.
2. Tria Beauty, Inc. [US20140214136A1, Pulse Width Modulation Control for Battery-Powered Laser Device](https://patents.google.com/patent/US20140214136A1/en). Primary patent; supports the direct high-current battery/laser-drive architecture and example single 18650-type lithium-manganese cell parameters. Patent embodiments are not proof of the exact shipped Precision configuration.
3. eBay seller toninonet. [Tria Precision battery replacement diagnostic service listing, item 255665106179](https://www.ebay.com/itm/255665106179). Accessed 2026-07-18; supports the service identity and the listing photograph of original pack TB P#11777B-02. The listing does not identify the replacement cell installed.
4. Recell Online / Batt.co.jp. [TB P#11777B-02 Tria Precision battery recell service](https://www.batt.co.jp/products/detail/6530). Accessed 2026-07-18; model-specific commercial service evidence for original 3.6 V, 1950 mAh lithium-ion specification and model 11777C-03 compatibility.
5. David Theuerkauf and Lukas Swan. [Characteristics of Open Circuit Voltage Relaxation in Lithium-Ion Batteries for the Purpose of State of Charge and State of Health Analysis](https://www.mdpi.com/2313-0105/8/8/77). *Batteries* 2022;8(8):77. Peer-reviewed mechanism evidence that lithium-ion terminal voltage relaxes toward a resting open-circuit value after current is interrupted; it does not diagnose this device.
6. Texas Instruments. [BQ77904/BQ77905 Lithium-Ion Battery Protector Data Sheet](https://www.ti.com/lit/ds/symlink/bq77905.pdf), sections 8.3.2.4–8.3.2.9. Primary component documentation showing that generic lithium-ion protectors may recover overcurrent/short-circuit states through timers and/or load-removal detection. This is mechanism evidence only; it does not show that Tria used this TI component.
