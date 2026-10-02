(() => {
  "use strict";

  const $ = id => document.getElementById(id);
  const ANCHORS = [[0, 0], [40, 3], [60, 5], [100, 8], [200, 16], [500, 40]];
  const OBSERVED_PH = [4.58, 4.95];
  const GENERATOR_SALT_G_L = 2;
  const GENERATOR_VINEGAR_ML_L = 5;
  const MARKET_SALT_G_L = 0.6;
  const SALT_CONDUCTIVITY_EXPONENT = 0.95;
  const FAC_LOW_FACTOR = 0.8;
  const FAC_HIGH_FACTOR = 1.4;
  const DEFAULT_BENCHMARK = "chloe";
  const CHLOE_REVIEW = { volume: 500, fac: 400, ph: 4.5, time: 15, salt: 3, saltType: "non-iodized table salt", vinegar: 1.25 };
  const CHLOE_USER_CALIBRATION = {
    volume: 250,
    fac: 300,
    ph: 4.5,
    time: 15,
    salt: 1.5,
    vinegar: 0.625,
    note: "User-supplied 2026-08-27 reproduction; FAC and pH are approximate visual readings"
  };

  const benchmarkMeta = {
    manual: { rate: GENERATOR_SALT_G_L, vinegarRate: GENERATOR_VINEGAR_ML_L, label: "Eco One documented generator feed", title: "Eco One documented recipe", experimental: false },
    market: { rate: MARKET_SALT_G_L, vinegarRate: GENERATOR_VINEGAR_ML_L, label: "market-median experimental generator feed", title: "Market-salt experimental recipe", experimental: true },
    chloe: {
      rate: CHLOE_REVIEW.salt / (CHLOE_REVIEW.volume / 1000),
      vinegarRate: CHLOE_REVIEW.vinegar / (CHLOE_REVIEW.volume / 1000),
      label: "Amazon/Chloe working generator feed",
      title: "Amazon/Chloe recipe · default observed-rate calibration",
      experimental: true,
      review: true,
      sourceVolume: CHLOE_REVIEW.volume,
      sourceFac: CHLOE_REVIEW.fac,
      sourcePh: CHLOE_REVIEW.ph,
      sourceTime: CHLOE_REVIEW.time,
      calibration: CHLOE_USER_CALIBRATION
    }
  };

  const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
  const near = (a, b, tolerance = 0.001) => Math.abs(a - b) < tolerance;
  const num = id => {
    const node = $(id);
    if (!node || node.value.trim() === "") return null;
    const value = Number(node.value);
    return Number.isFinite(value) ? value : NaN;
  };

  function baseTime(fac) {
    if (fac <= 0) return 0;
    for (let i = 1; i < ANCHORS.length; i += 1) {
      const [fac0, time0] = ANCHORS[i - 1];
      const [fac1, time1] = ANCHORS[i];
      if (fac <= fac1) return time0 + ((fac - fac0) / (fac1 - fac0)) * (time1 - time0);
    }
    return 40 + (fac - 500) / 12.5;
  }

  function exactOneLiterProgram(fac) {
    const programs = {
      40: ["Setting 1", "one 3-minute cycle"],
      60: ["Setting 2", "one 5-minute cycle"],
      100: ["Setting 3", "one 8-minute cycle"],
      200: ["Setting 3 × 2", "two 8-minute cycles"],
      500: ["Setting 3 × 5", "five 8-minute cycles · current product-page endpoint"]
    };
    return programs[fac] || null;
  }

  function deviceProgram(volume, fac, time, experimental = false, review = false) {
    if (review) {
      return {
        name: `${time.toFixed(2)} min`,
        note: "Amazon/Chloe default observed-rate estimate · requires documented manual stop and fresh FAC/pH measurement",
        builtIn: false
      };
    }
    if (experimental) {
      const fullCycles = Math.floor(time / 8);
      const remainder = time - fullCycles * 8;
      const parts = [];
      if (fullCycles > 0) parts.push(`Setting 3 × ${fullCycles}`);
      if (remainder >= 0.05) parts.push(`${remainder.toFixed(2)} min partial`);
      return {
        name: parts.join(" + ") || `${time.toFixed(2)} min`,
        note: "experimental conductivity-scaled plan · final partial interval requires documented manual stop",
        builtIn: remainder < 0.05
      };
    }
    if (volume === 1000) {
      const exact = exactOneLiterProgram(fac);
      if (exact) return { name: exact[0], note: exact[1], builtIn: true };
    }
    if (volume === 500 && fac === 200) {
      return { name: "Setting 3", note: "published 500 mL / 200 ppm / 8-minute point", builtIn: true };
    }
    return {
      name: `${time.toFixed(2)} min`,
      note: "continuous estimate · requires documented manual-stop capability",
      builtIn: false
    };
  }

  function plan() {
    return {
      volume: num("volume"),
      targetFac: num("targetFac"),
      targetPh: num("targetPh"),
      waterPh: num("waterPh"),
      benchmark: $("saltBenchmark").value in benchmarkMeta ? $("saltBenchmark").value : DEFAULT_BENCHMARK
    };
  }

  function model() {
    const input = plan();
    const volumeL = input.volume / 1000;
    const base = baseTime(input.targetFac);
    const benchmark = benchmarkMeta[input.benchmark];
    const reviewDerived = Boolean(benchmark.review);
    const saltTimeFactor = reviewDerived ? null : Math.pow(GENERATOR_SALT_G_L / benchmark.rate, SALT_CONDUCTIVITY_EXPONENT);
    const reviewCalibration = reviewDerived ? benchmark.calibration : null;
    const reviewFacFactor = reviewDerived ? input.targetFac / reviewCalibration.fac : null;
    const reviewClaimTime = reviewDerived
      ? benchmark.sourceTime * (input.volume / benchmark.sourceVolume) * (input.targetFac / benchmark.sourceFac)
      : null;
    const time = reviewDerived
      ? reviewCalibration.time * (input.volume / reviewCalibration.volume) * reviewFacFactor
      : base * volumeL * saltTimeFactor;
    const exactAnchor = ANCHORS.some(([fac]) => fac === input.targetFac);
    const officialOneLiter = !benchmark.experimental && input.volume === 1000 && exactAnchor;
    const officialHalfLiter = !benchmark.experimental && input.volume === 500 && input.targetFac === 200;
    return {
      ...input,
      volumeL,
      baseTime: base,
      time,
      salt: benchmark.rate * volumeL,
      vinegar: benchmark.vinegarRate * volumeL,
      benchmarkRate: benchmark.rate,
      benchmarkAmount: benchmark.rate * volumeL,
      benchmarkLabel: benchmark.label,
      benchmarkTitle: benchmark.title,
      benchmarkVinegarRate: benchmark.vinegarRate,
      vinegarLabel: reviewDerived ? "Vinegar (review amount; acidity unspecified)" : "5% distilled white vinegar",
      experimentalSalt: benchmark.experimental && !reviewDerived,
      reviewDerived,
      reviewAnchor: reviewDerived ? { ...CHLOE_REVIEW } : null,
      reviewCalibration: reviewDerived ? { ...reviewCalibration } : null,
      reviewFacFactor,
      reviewClaimTime,
      reviewCalibrationFacRate: reviewDerived ? reviewCalibration.fac / reviewCalibration.time : null,
      reviewCalibrationMassRate: reviewDerived ? reviewCalibration.fac * (reviewCalibration.volume / 1000) / reviewCalibration.time : null,
      reviewClaimFacRate: reviewDerived ? CHLOE_REVIEW.fac / CHLOE_REVIEW.time : null,
      reviewClaimMassRate: reviewDerived ? CHLOE_REVIEW.fac * (CHLOE_REVIEW.volume / 1000) / CHLOE_REVIEW.time : null,
      saltTimeFactor,
      nominalFacMassMg: input.targetFac * volumeL,
      exactAnchor,
      officialOneLiter,
      officialHalfLiter,
      official: officialOneLiter || officialHalfLiter,
      program: deviceProgram(input.volume, input.targetFac, time, benchmark.experimental && !reviewDerived, reviewDerived),
      outputWatts: null
    };
  }

  function svg(tag, attrs = {}, text = "") {
    const node = document.createElementNS("http://www.w3.org/2000/svg", tag);
    Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, value));
    if (text !== "") node.textContent = text;
    return node;
  }

  function drawFac(m) {
    const root = $("facChart");
    root.replaceChildren();
    const left = 48, right = 500, top = 22, bottom = 252;
    const width = right - left, height = bottom - top;
    const maxTime = Math.max(1, m.time);
    const maxY = Math.max(60, m.targetFac * 1.55);
    const x = time => left + (time / maxTime) * width;
    const y = value => bottom - (value / maxY) * height;

    [0, 0.25, 0.5, 0.75, 1].forEach(fraction => {
      const value = maxY * fraction;
      root.append(svg("line", { x1: left, y1: y(value), x2: right, y2: y(value), stroke: "#e1ece8" }));
      root.append(svg("text", { x: left - 7, y: y(value) + 4, "text-anchor": "end", fill: "#60716d", "font-size": "10" }, Math.round(value)));
      const time = maxTime * fraction;
      root.append(svg("line", { x1: x(time), y1: top, x2: x(time), y2: bottom, stroke: "#edf3f1" }));
      root.append(svg("text", { x: x(time), y: bottom + 18, "text-anchor": "middle", fill: "#60716d", "font-size": "10" }, time.toFixed(time < 10 ? 1 : 0)));
    });

    const points = Array.from({ length: 41 }, (_, index) => {
      const fraction = index / 40;
      return [x(m.time * fraction), y(m.targetFac * fraction)];
    });
    const upper = points.map(([xx], index) => `${xx},${y(m.targetFac * (index / 40) * FAC_HIGH_FACTOR)}`).join(" ");
    const lower = [...points].reverse().map(([xx], reverseIndex) => {
      const fraction = (40 - reverseIndex) / 40;
      return `${xx},${y(m.targetFac * fraction * FAC_LOW_FACTOR)}`;
    }).join(" ");
    root.append(svg("polygon", { points: `${upper} ${lower}`, fill: "#a7d8c8", opacity: ".38" }));
    root.append(svg("polyline", { points: points.map(point => point.join(",")).join(" "), fill: "none", stroke: "#0f766e", "stroke-width": "4", "stroke-linecap": "round" }));
    root.append(svg("circle", { cx: x(m.time), cy: y(m.targetFac), r: 6, fill: "#0f766e", stroke: "#fff", "stroke-width": "2" }));
    root.append(svg("text", { x: right, y: 14, "text-anchor": "end", fill: "#0f766e", "font-size": "11", "font-weight": "700" }, `${m.targetFac} ppm at ${m.time.toFixed(2)} min`));
    root.append(svg("text", { x: left, y: 14, fill: "#60716d", "font-size": "10" }, "ppm"));
    root.append(svg("text", { x: right, y: bottom + 33, "text-anchor": "end", fill: "#60716d", "font-size": "10" }, "minutes"));
  }

  function drawPh(m) {
    const root = $("phChart");
    root.replaceChildren();
    const left = 48, right = 500, top = 22, bottom = 252;
    const width = right - left, height = bottom - top;
    const maxTime = Math.max(20, m.time);
    const minY = 3.5, maxY = 7;
    const x = time => left + (time / maxTime) * width;
    const y = value => bottom - ((value - minY) / (maxY - minY)) * height;

    [4, 4.5, 5, 5.5, 6, 6.5].forEach(value => {
      root.append(svg("line", { x1: left, y1: y(value), x2: right, y2: y(value), stroke: "#eee8f6" }));
      root.append(svg("text", { x: left - 7, y: y(value) + 4, "text-anchor": "end", fill: "#60716d", "font-size": "10" }, `pH ${value}`));
    });
    [0, 5, 10, 15, 20].filter(time => time <= maxTime).forEach(time => {
      root.append(svg("line", { x1: x(time), y1: top, x2: x(time), y2: bottom, stroke: "#f0edf6" }));
      root.append(svg("text", { x: x(time), y: bottom + 18, "text-anchor": "middle", fill: "#60716d", "font-size": "10" }, String(time)));
    });
    if (maxTime > 20) {
      root.append(svg("line", { x1: x(maxTime), y1: top, x2: x(maxTime), y2: bottom, stroke: "#f0edf6" }));
      root.append(svg("text", { x: x(maxTime), y: bottom + 18, "text-anchor": "middle", fill: "#60716d", "font-size": "10" }, maxTime.toFixed(0)));
    }

    root.append(svg("line", { x1: left, y1: y(m.targetPh), x2: right, y2: y(m.targetPh), stroke: "#6b55a3", "stroke-width": "3" }));
    const observedX = x(20);
    root.append(svg("line", { x1: observedX, y1: y(OBSERVED_PH[0]), x2: observedX, y2: y(OBSERVED_PH[1]), stroke: "#c6841d", "stroke-width": "12", "stroke-linecap": "round", opacity: ".75" }));
    OBSERVED_PH.forEach(value => root.append(svg("circle", { cx: observedX, cy: y(value), r: 5, fill: "#c6841d", stroke: "#fff", "stroke-width": "2" })));
    root.append(svg("line", { x1: x(m.time), y1: top, x2: x(m.time), y2: bottom, stroke: "#2563eb", "stroke-width": "2", "stroke-dasharray": "5 5" }));
    root.append(svg("text", { x: left, y: 14, fill: "#6b55a3", "font-size": "11", "font-weight": "700" }, `target pH ${m.targetPh.toFixed(2)}`));
    root.append(svg("text", { x: right, y: 14, "text-anchor": "end", fill: "#9a5b08", "font-size": "11", "font-weight": "700" }, "observed at 20 min: 4.58–4.95"));
    root.append(svg("text", { x: right, y: bottom + 33, "text-anchor": "end", fill: "#60716d", "font-size": "10" }, "minutes"));
  }

  function methodComplete() {
    return Boolean($("facMethod").value && $("phMethod").value);
  }

  function state() {
    const m = model();
    const fac = num("measuredFac"), ph = num("measuredPh");
    const facMethod = $("facMethod").value, phMethod = $("phMethod").value;
    if (Number.isNaN(fac) || Number.isNaN(ph) || (fac !== null && (fac < 0 || fac > 2000)) || (ph !== null && (ph < 0 || ph > 14))) return { kind: "bad", eye: "Invalid entry", title: "Check the measurement entries", body: "Use numeric readings inside each method’s documented range.", code: "invalid" };
    if (fac === null && ph === null) return { kind: "info", eye: "Recipe only", title: "Make the batch, then enter both measurements", body: "Before FAC and pH are measured together, the graphs remain planning evidence.", code: "missing-both" };
    if (fac === null || ph === null) return { kind: "info", eye: "Incomplete measurement", title: `Enter the missing ${fac === null ? "FAC" : "pH"} result`, body: "A favorable value on one axis cannot classify the batch.", code: "missing-one" };
    if (!methodComplete()) return { kind: "info", eye: "Incomplete method record", title: "Choose both measurement methods", body: "Method range and resolution change interpretation confidence.", code: "missing-method" };
    if (facMethod === "bad" || phMethod === "bad") return { kind: "bad", eye: "Measurement stop", title: "At least one method cannot resolve this batch", body: "Repeat the measurement with suitable-range methods; do not adjust the finished batch.", code: "bad-method" };
    if (ph <= 3 || ph > 7) return { kind: "bad", eye: "Stop", title: "Final pH is outside the project record envelope", body: "Do not counter-adjust the completed chlorine-containing batch.", code: "ph-stop" };
    if (ph < 4 || ph > 6.5) return { kind: "warn", eye: "Investigate", title: "Final pH misses the documented working range", body: "Keep the record for next-fresh-batch review; do not rescue the finished batch.", code: "ph-caution" };
    if (fac / m.targetFac < 0.8 || fac / m.targetFac > 1.2) return { kind: "warn", eye: "Outside FAC comparison band", title: `Measured FAC is more than 20% from ${m.targetFac} ppm`, body: "This is a process difference, not a skin-safety verdict. Bring the paired result to chat.", code: "fac-caution" };
    if (Math.abs(ph - m.targetPh) > 0.2) return { kind: "warn", eye: "Outside selected pH target", title: `Measured pH is more than 0.2 from ${m.targetPh.toFixed(2)}`, body: "The pH selector is a comparison target, not an acid-dose formula. Review only a separate fresh batch.", code: "ph-target-caution" };
    if (facMethod === "coarse" || phMethod === "coarse") return { kind: "warn", eye: "Low-resolution record", title: "The readings land near plan but are coarsely resolved", body: "Repeat with suitable-range methods before treating the process as calibrated.", code: "coarse" };
    return { kind: "ok", eye: "Inside selected project bands", title: "Record this paired result", body: "FAC is within ±20% and pH within ±0.2 of the selected targets. This remains a process record, not a product certificate.", code: "preferred" };
  }

  function confidence() {
    const fac = num("measuredFac"), ph = num("measuredPh");
    const facMethod = $("facMethod").value, phMethod = $("phMethod").value;
    const repeats = Number($("repeatCount").value);
    if (fac === null && ph === null) return ["Not assessed", "Confidence describes measured process repeatability—not skin safety."];
    if (fac === null || ph === null || !facMethod || !phMethod) return ["Incomplete", "Both axes and both methods are required."];
    if (facMethod === "bad" || phMethod === "bad") return ["Not interpretable", "At least one method did not cover the result."];
    if (repeats >= 3 && facMethod === "fit" && phMethod === "meter") return ["Higher process-repeatability confidence", "Three or more matching fresh batches with suitable methods."];
    if (repeats >= 2 && facMethod === "fit" && (phMethod === "meter" || phMethod === "strip")) return ["Moderate process-repeatability confidence", "At least two matching fresh paired batches with suitable methods."];
    return ["Low process-repeatability confidence", "One paired batch or a coarse method cannot establish repeatability."];
  }

  function updateMarkers(m) {
    const fac = num("measuredFac"), ph = num("measuredPh");
    const facMarker = $("facMarker"), phMarker = $("phMarker");
    if (fac === null || Number.isNaN(fac)) {
      facMarker.classList.add("hidden");
      $("facBandRead").textContent = `Measure against ${m.targetFac} ppm`;
    } else {
      facMarker.classList.remove("hidden");
      facMarker.style.left = `${clamp((fac / (m.targetFac * 2)) * 100, 0, 100)}%`;
      $("facBandRead").textContent = `Measured ${fac} ppm · target ${m.targetFac}`;
    }
    if (ph === null || Number.isNaN(ph)) {
      phMarker.classList.add("hidden");
      $("phBandRead").textContent = `Measure against pH ${m.targetPh.toFixed(2)}`;
    } else {
      phMarker.classList.remove("hidden");
      phMarker.style.left = `${clamp(((ph - 3) / 4) * 100, 0, 100)}%`;
      $("phBandRead").textContent = `Measured ${ph} · target ${m.targetPh.toFixed(2)}`;
    }
  }

  function renderDecision(m) {
    const result = state(), processConfidence = confidence();
    const node = $("decision");
    node.className = `decision ${result.kind}`;
    node.innerHTML = `<div class="eyebrow">${result.eye}</div><h3>${result.title}</h3><p>${result.body}</p>`;
    $("confidence").innerHTML = `<div class="eyebrow">Process confidence</div><h3>${processConfidence[0]}</h3><p>${processConfidence[1]}</p>`;
    updateMarkers(m);
  }

  function evidenceText(m) {
    if (m.reviewDerived) {
      const anchor = m.reviewAnchor;
      const calibration = m.reviewCalibration;
      const facAdjustment = near(m.targetFac, calibration.fac)
        ? "The selected ≈300 ppm target uses the observed-rate anchor directly."
        : `Changing the FAC target applies a local-rate adjustment of ${m.reviewFacFactor.toFixed(2)}× from the observed ≈300 ppm point; that adjustment is a planning estimate, not a second measurement.`;
      return `The Amazon/Chloe recipe is the planner’s default working calibration. Your supplied reproduction is logged as approximately ${calibration.fac} ppm and pH ${calibration.ph.toFixed(1)} after ${calibration.time.toFixed(2)} minutes at ${calibration.volume} mL, assuming ${calibration.salt.toFixed(2)} g salt and ${calibration.vinegar.toFixed(3)} mL vinegar were used. That establishes an observed rate of about ${m.reviewCalibrationFacRate.toFixed(1)} ppm/min in ${calibration.volume} mL, or about ${m.reviewCalibrationMassRate.toFixed(2)} mg FAC-equivalent/min total. Every volume and FAC calculation in this recipe uses that point first: at ${m.volume} mL, the working time is ${m.time.toFixed(2)} minutes. Chloe’s original source record reports ${anchor.volume} mL, ${anchor.salt.toFixed(2)} g ${anchor.saltType}, ${anchor.vinegar.toFixed(2)} mL vinegar, and ${anchor.time.toFixed(2)} minutes near ${anchor.fac} ppm/pH ${anchor.ph.toFixed(1)}; its ${m.reviewClaimTime.toFixed(2)}-minute extrapolation is retained as historical context, not the active calculation. ${facAdjustment} The vinegar acidity and device compatibility remain undocumented; measure final FAC and pH.`;
    }
    if (m.experimentalSalt) return `At ${m.benchmarkRate.toFixed(2)} g/L salt, ${m.time.toFixed(2)} minutes equals the documented ${m.baseTime.toFixed(2)}-minute 1 L charge curve × ${(m.volumeL).toFixed(3)} volume factor × ${m.saltTimeFactor.toFixed(2)} conductivity factor. The factor assumes constant-voltage-like behavior and unchanged current efficiency; measure FAC because Eco One has not published this low-salt calibration.`;
    if (m.officialOneLiter) return `At 1,000 mL and ${m.targetFac} ppm, ${m.time.toFixed(2)} minutes is a direct published endpoint. The selected program is ${m.program.name}. No wattage correction is applied because output watts are not disclosed. This timer uses the documented 2.00 g/L feed.`;
    if (m.officialHalfLiter) return "The 500 mL / 200 ppm / 8-minute result is separately published and matches the volume-charge model at the documented 2.00 g/L feed. Final FAC and pH still require measurement.";
    if (m.volume < 500) return `At ${m.volume} mL, ${m.time.toFixed(2)} minutes is below the smallest published 500 mL validation point. Treat it as a wider extrapolation and confirm electrode immersion and manual stopping. Generator feed is 2.00 g/L.`;
    return `At ${m.volume} mL and ${m.targetFac} ppm, ${m.time.toFixed(2)} minutes is interpolated and/or volume-scaled from published charge-time anchors at 2.00 g/L feed. Output watts are unknown, so no power multiplier is used.`;
  }

  function update() {
    const m = model();
    $("volumeOut").textContent = `${m.volume.toLocaleString()} mL`;
    $("targetOut").textContent = `${m.targetFac} ppm`;
    $("targetPhOut").textContent = m.targetPh.toFixed(2);
    $("waterPhOut").textContent = m.waterPh.toFixed(2);
    $("waterRecipe").textContent = `${m.volume.toLocaleString()} mL`;
    $("waterMassOut").textContent = `≈ ${m.volume.toLocaleString()} g purified water`;
    $("saltOut").textContent = `${m.salt.toFixed(2)} g`;
    $("saltRateNote").textContent = m.reviewDerived
      ? `working recipe · ${m.benchmarkRate.toFixed(2)} g/L`
      : m.experimentalSalt
      ? `experimental · ${m.benchmarkRate.toFixed(2)} g/L`
      : `documented · ${m.benchmarkRate.toFixed(2)} g/L`;
    $("vinegarLabel").textContent = m.vinegarLabel;
    $("vinegarOut").textContent = `${m.vinegar.toFixed(2)} mL`;
    $("vinegarRateNote").textContent = m.reviewDerived
      ? `working recipe · ${m.benchmarkVinegarRate.toFixed(2)} mL/L`
      : `manual-locked · ${m.benchmarkVinegarRate.toFixed(2)} mL/L`;
    $("targetPhNote").textContent = m.reviewDerived
      ? `The default working calibration uses the observed pH near ${m.reviewAnchor.ph.toFixed(1)} as a comparison target—not a vinegar-dose control. Vinegar acidity and salt/volume execution still require a finished-batch measurement.`
      : "The pH target is continuously adjustable in 0.01 increments, but it is a comparison target—not a vinegar-dose control. The selected recipe keeps its vinegar amount locked to its mode and requires a final measurement.";
    $("programOut").textContent = `${m.time.toFixed(2)} min`;
    $("programNote").textContent = m.reviewDerived ? "default observed-rate estimate" : (m.official ? "published device endpoint" : (m.experimentalSalt ? "experimental salt/conductivity estimate" : "interpolated / volume-scaled estimate"));
    $("recipeFacOut").textContent = `${m.targetFac} ppm`;
    $("recipePhOut").textContent = m.targetPh.toFixed(2);
    $("benchmarkSaltOut").textContent = `${m.benchmarkRate.toFixed(2)} g/L`;
    $("benchmarkSaltNote").textContent = `${m.benchmarkLabel} · ${m.benchmarkAmount.toFixed(2)} g at selected volume`;
    $("timingBasisLabel").textContent = m.reviewDerived ? "Observed-rate timing" : "Salt-time factor";
    $("saltTimerOut").textContent = m.reviewDerived ? "local" : `${m.saltTimeFactor.toFixed(2)}×`;
    $("saltTimerNote").textContent = m.reviewDerived
      ? "default: 250 mL / ≈300 ppm / 15 min observation"
      : m.experimentalSalt
      ? `conductivity model · exponent ${SALT_CONDUCTIVITY_EXPONENT.toFixed(2)}`
      : "published 2.00 g/L baseline";
    $("deviceProgramOut").textContent = m.program.name;
    $("deviceProgramNote").textContent = m.program.note;
    $("facChartClass").textContent = m.reviewDerived ? "default observed-rate calibration" : (m.official ? "published endpoint" : (m.experimentalSalt ? "low-salt conductivity estimate" : "scaled sensitivity"));
    $("graphNote").innerHTML = m.reviewDerived
      ? `<b>Read the graphs this way:</b> the central line is the default observed-rate calibration from your supplied ${m.reviewCalibration.volume} mL / ≈${m.reviewCalibration.fac} ppm / ${m.reviewCalibration.time}-minute batch, assuming the working recipe used ${m.reviewCalibration.salt.toFixed(2)} g salt and ${m.reviewCalibration.vinegar.toFixed(3)} mL vinegar. Chloe’s original ${m.reviewAnchor.volume} mL / ≈${m.reviewAnchor.fac} ppm / ${m.reviewAnchor.time}-minute record remains source context only. The shaded band is a sensitivity scenario; test the actual batch immediately.`
      : m.experimentalSalt
      ? `<b>Read the graphs this way:</b> documented mode is anchored directly to the 2.00 g/L programs. Experimental mode stretches the time axis with the 0.95 conductivity exponent while holding current efficiency constant. This is an unvalidated sensitivity scenario; low-salt efficiency, controller behavior, and electrode mass transport remain unmeasured. Test the actual batch immediately.`
      : `<b>Read the graphs this way:</b> documented mode is anchored directly to the 2.00 g/L programs and then volume-scaled between published points. The 0.8–1.4× band is a sensitivity scenario, not a confidence interval. Test the actual batch immediately.`;
    $("evidenceTitle").textContent = m.reviewDerived ? "Default Amazon/Chloe observed calibration" : (m.experimentalSalt ? "Experimental salt-corrected timing" : (m.official ? "Published timing endpoint" : (m.volume < 500 ? "Below published volume check" : "Interpolated / volume-scaled timing")));
    $("evidenceText").textContent = evidenceText(m);
    $("effectVolume").textContent = m.reviewDerived
      ? `At ${m.volume.toLocaleString()} mL, the working Amazon/Chloe ratio produces ${m.salt.toFixed(2)} g salt and ${m.vinegar.toFixed(3)} mL vinegar. Time scales from the observed 250 mL point to ${m.time.toFixed(2)} minutes; final FAC and pH still require measurement.`
      : `At ${m.volume.toLocaleString()} mL, the ${m.targetFac} ppm target contains ${m.nominalFacMassMg.toFixed(1)} mg nominal FAC and maps to ${m.time.toFixed(2)} minutes. Generator salt remains ${m.salt.toFixed(2)} g.`;
    $("effectFac").textContent = m.reviewDerived
      ? `The default local rate is approximately ${m.reviewCalibrationFacRate.toFixed(1)} ppm/min in ${m.reviewCalibration.volume} mL. At ${m.volume} mL, the ${m.targetFac} ppm plan maps to ${m.time.toFixed(2)} minutes; changing volume or target changes the estimate, not the measured result.`
      : `The ${m.targetFac} ppm target maps to ${m.baseTime.toFixed(2)} minutes at 1 L and ${m.time.toFixed(2)} minutes at ${m.volume} mL. Real efficiency can depart from the model.`;
    $("effectPh").textContent = `Target pH ${m.targetPh.toFixed(2)} changes the measured-result comparison only. Vinegar remains ${m.benchmarkVinegarRate.toFixed(2)} mL/L${m.reviewDerived ? " at the review-reported acidity-unknown rate" : " because no validated dose-to-final-pH curve was found"}.`;
    $("effectSalt").textContent = m.reviewDerived
      ? `The default Amazon/Chloe recipe locks ${m.benchmarkRate.toFixed(2)} g/L salt and ${m.benchmarkVinegarRate.toFixed(3)} mL/L vinegar. The observed ≈${m.reviewCalibration.fac} ppm point is the primary rate anchor for this locked recipe when the same scaled ingredients are used.`
      : m.experimentalSalt
      ? `Reducing feed from ${GENERATOR_SALT_G_L.toFixed(2)} to ${m.benchmarkRate.toFixed(2)} g/L applies a ${m.saltTimeFactor.toFixed(2)}× time factor. This assumes current follows dilute-solution conductivity and efficiency stays constant; measured FAC must recalibrate the next fresh batch.`
      : `At ${GENERATOR_SALT_G_L.toFixed(2)} g/L the salt-time factor is 1.00× and the published timer applies. Final FAC still owns the result.`;
    $("timingAssumption").innerHTML = m.reviewDerived
      ? `<b>Default Amazon/Chloe observed-rate assumption:</b> every batch generated by this recipe uses your supplied ${m.reviewCalibration.volume} mL / ≈${m.reviewCalibration.fac} ppm / ${m.reviewCalibration.time}-minute result as its primary calibration point. It therefore uses <code>time = 15 × volume / 250 × target FAC / 300</code>; more than 250 mL takes proportionally longer and less takes proportionally less. The original review claim (${m.reviewAnchor.volume} mL / ≈${m.reviewAnchor.fac} ppm / ${m.reviewAnchor.time} minutes) is retained as historical source context. The vinegar amount is locked to the scaled review ratio, but its acidity is unspecified; final FAC and pH own the result.`
      : `<b>Salt timing assumption:</b> electrochemical product follows charge passed and current efficiency. For the experimental mode, the calculator estimates conductivity ∝ salt concentration<sup>0.95</sup>, current ∝ conductivity at fixed voltage, and time ∝ 1/current. Therefore <code>time factor = (2.00 / selected g/L)<sup>0.95</sup></code>. At 0.60 g/L this is 3.14×. If Eco One regulates current, reaches a voltage limit, or loses efficiency at low chloride, the real factor can differ; FAC measurement owns the result.`;
    $("recipeInputStep").innerHTML = m.reviewDerived
      ? `<b>Weigh the selected salt.</b> Use the displayed ${m.salt.toFixed(2)} g ${m.reviewAnchor.saltType} and ${m.vinegar.toFixed(3)} mL vinegar for this ${m.volume.toLocaleString()} mL Amazon/Chloe working batch. The default calibration is tied to ${m.reviewCalibration.salt.toFixed(2)} g salt and ${m.reviewCalibration.vinegar.toFixed(3)} mL vinegar at 250 mL; using the original full review amounts there would be a different recipe. The review does not identify vinegar acidity; use this route only when the exact device manual permits it.`
      : `<b>Weigh the selected salt.</b> Use the displayed generator NaCl amount: 2.00 g/L in documented mode or 0.60 g/L in market-salt mode. Add the displayed 5.00 mL/L of 5% distilled white vinegar before electrolysis only when the exact device manual permits it. Do not use cleaning vinegar or concentrated acid.`;
    $("recipeTimingStep").innerHTML = m.reviewDerived
      ? `<b>Run the displayed program.</b> The ${m.time.toFixed(2)}-minute program is the primary observed-rate estimate from your approximate ${m.reviewCalibration.fac} ppm result at ${m.reviewCalibration.volume} mL. The original review’s ${m.reviewAnchor.time}-minute claim is historical context, not the active timing basis; use documented manual stopping plus fresh FAC/pH measurement.`
      : `<b>Run the displayed program.</b> Exact manual programs are labeled. Experimental timing may combine complete 8-minute cycles with a final partial interval and therefore requires documented manual stopping.`;

    document.querySelectorAll("[data-fac]").forEach(button => {
      const active = Number(button.dataset.fac) === m.targetFac;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    document.querySelectorAll("[data-ph]").forEach(button => {
      const active = near(Number(button.dataset.ph), m.targetPh, 0.0001);
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    document.querySelectorAll("[data-benchmark]").forEach(button => {
      const active = button.dataset.benchmark === m.benchmark;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
    drawFac(m);
    drawPh(m);
    renderDecision(m);
  }

  function report() {
    const m = model(), fac = num("measuredFac"), ph = num("measuredPh"), result = state();
    const note = $("batchId").value.trim();
    const ratioLabel = m.reviewDerived ? "working-locked" : (m.experimentalSalt ? "experimental" : "documented");
    const saltDescription = m.reviewDerived ? `${m.salt.toFixed(2)} g ${m.reviewAnchor.saltType}` : `${m.salt.toFixed(2)} g`;
    const timingLine = m.reviewDerived
      ? `Default observed-rate calibration: ${m.reviewCalibration.volume} mL / approximately ${m.reviewCalibration.fac} ppm / ${m.reviewCalibration.time} minutes; local rate ${m.reviewCalibrationFacRate.toFixed(1)} ppm/min (${m.reviewCalibrationMassRate.toFixed(2)} mg FAC-equivalent/min total); FAC factor ${m.reviewFacFactor.toFixed(2)}×`
      : `Salt-time factor: ${m.saltTimeFactor.toFixed(2)}× (${m.experimentalSalt ? `conductivity exponent ${SALT_CONDUCTIVITY_EXPONENT.toFixed(2)}; constant-voltage/constant-efficiency scenario` : "published 2.00 g/L baseline"})`;
    const timingLabel = m.reviewDerived ? "default observed-rate estimate" : (m.official ? "published endpoint" : (m.experimentalSalt ? "experimental salt/conductivity estimate" : "interpolated / volume-scaled estimate"));
    const boundaryTiming = m.reviewDerived
      ? `Timing uses the primary user observation (${m.reviewCalibration.volume} mL, approximately ${m.reviewCalibration.fac} ppm, ${m.reviewCalibration.time} minutes), proportional volume scaling, and a local FAC-rate adjustment. The original Amazon review claim (${m.reviewAnchor.volume} mL, approximately ${m.reviewAnchor.fac} ppm, ${m.reviewAnchor.time} minutes) would predict ${m.reviewClaimTime.toFixed(2)} minutes for the current selection and is retained as historical source context.`
      : `Timing uses published FAC/time anchors at 2.00 g/L plus volume scaling${m.experimentalSalt ? ` and the illustrative salt factor (2.00 / ${m.benchmarkRate.toFixed(2)})^${SALT_CONDUCTIVITY_EXPONENT.toFixed(2)}` : ""}.`;
    return [
      "HOCl RECIPE-DEVELOPER REPORT", "", "PLANNED FRESH BATCH",
      `Water: ${m.volume} mL`,
      `Target FAC: ${m.targetFac} ppm`,
      `Target final pH: ${m.targetPh.toFixed(2)}`,
      `Starting-water pH record: ${m.waterPh.toFixed(2)}`,
      `Recipe mode: ${m.benchmarkTitle}`,
      `Generator NaCl: ${saltDescription} (${m.benchmarkRate.toFixed(2)} g/L ${ratioLabel} ratio)`,
      `${m.vinegarLabel}: ${m.vinegar.toFixed(2)} mL (${m.benchmarkVinegarRate.toFixed(2)} mL/L ${m.reviewDerived ? "working-locked; acidity unspecified" : "manual-locked ratio"})`,
      timingLine,
      `Planned time: ${m.time.toFixed(2)} minutes (${timingLabel})`,
      `Device program: ${m.program.name} — ${m.program.note}`,
      "Power correction: none; DC output voltage/current/watts not disclosed",
      `Calibration note: ${m.reviewDerived ? `${m.reviewCalibration.note}; primary working rate for this recipe` : "not applicable"}`, "", "MEASURED RESULT",
      `FAC: ${fac === null ? "not entered" : `${fac} ppm`}`,
      `Final pH: ${ph === null ? "not entered" : ph}`,
      `FAC method: ${$("facMethod").selectedOptions[0].textContent}`,
      `pH method: ${$("phMethod").selectedOptions[0].textContent}`,
      `Matching fresh-batch repeats: ${$("repeatCount").value}`,
      `Batch note: ${note || "none"}`,
      `UI state: ${result.eye} — ${result.title}`, "", "CHAT REQUEST",
      "Please review this paired result and help plan only the next fresh manual-compatible calibration batch. Do not recommend adding acid, salt, or other chemistry to the finished chlorine-containing batch.", "", "MODEL BOUNDARY",
      `${boundaryTiming} Electrochemical production depends on integrated current and current efficiency; Eco One controller behavior is unknown. No pH-time kinetics, wattage correction, skin safety, purity, sterility, preservation, shelf life, or efficacy is inferred.`
    ].join("\n");
  }

  async function copyReport() {
    try {
      await navigator.clipboard.writeText(report());
      $("shareStatus").textContent = "Copied. Paste this report into chat for next-fresh-batch review.";
    } catch (error) {
      const area = document.createElement("textarea");
      area.value = report();
      area.setAttribute("readonly", "");
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      const copied = document.execCommand("copy");
      area.remove();
      $("shareStatus").textContent = copied ? "Copied. Paste this report into chat." : "Copy was blocked; use Download worksheet instead.";
    }
  }

  function download() {
    const blob = new Blob([report()], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = "hocl-skincare-calibration-report.txt";
    document.body.appendChild(anchor);
    anchor.click();
    anchor.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    $("shareStatus").textContent = "Downloaded hocl-skincare-calibration-report.txt.";
  }

  function test() {
    const ids = ["volume", "targetFac", "targetPh", "waterPh", "saltBenchmark", "measuredFac", "measuredPh", "facMethod", "phMethod"];
    const saved = Object.fromEntries(ids.map(id => [id, $(id).value]));
    const checks = [];
    const check = (name, pass) => checks.push([name, Boolean(pass)]);

    check("40 ppm anchor", near(baseTime(40), 3));
    check("60 ppm anchor", near(baseTime(60), 5));
    check("100 ppm anchor", near(baseTime(100), 8));
    check("200 ppm anchor", near(baseTime(200), 16));
    check("500 ppm anchor", near(baseTime(500), 40));

    const defaultPlan = model();
    check("default uses observed calibration", defaultPlan.benchmark === DEFAULT_BENCHMARK && near(defaultPlan.volume, 250) && near(defaultPlan.targetFac, 300) && near(defaultPlan.targetPh, 4.5) && near(defaultPlan.time, 15) && near(defaultPlan.salt, 1.5) && near(defaultPlan.vinegar, 0.625));

    $("saltBenchmark").value = DEFAULT_BENCHMARK; $("volume").value = "200"; $("targetFac").value = "300";
    const observedHalf = model();
    $("volume").value = "500";
    const observedDouble = model();
    check("observed-rate volume scaling", near(observedHalf.time, 12) && near(observedDouble.time, 30) && near(observedDouble.time, observedHalf.time * 2.5));
    $("targetFac").value = "400";
    check("observed-rate FAC scaling", near(model().time, 40));

    $("volume").value = "200"; $("targetFac").value = "100"; $("targetPh").value = "5.50"; $("waterPh").value = "7.00"; $("saltBenchmark").value = "manual";
    let minimum = model();
    check("200 mL scaling", near(minimum.time, 1.6) && near(minimum.salt, 0.4) && near(minimum.vinegar, 1));
    $("volume").value = "500";
    let half = model();
    check("half-volume scaling", near(half.time, 4) && near(half.salt, 1));
    $("targetFac").value = "200";
    half = model();
    check("published 500 mL point", half.officialHalfLiter && near(half.time, 8) && half.program.builtIn);
    $("volume").value = "1000"; $("targetFac").value = "100";
    const full = model();
    check("source-size identity", full.officialOneLiter && near(full.time, 8) && near(full.salt, 2) && near(full.vinegar, 5));

    $("volume").value = "537"; $("targetFac").value = "137"; $("targetPh").value = "5.43"; $("waterPh").value = "7.12";
    const continuous = model();
    check("continuous controls", continuous.volume === 537 && continuous.targetFac === 137 && near(continuous.targetPh, 5.43) && Number.isFinite(continuous.time));
    check("nonstandard program gate", !continuous.program.builtIn && continuous.program.note.includes("manual-stop"));

    $("volume").value = "1000"; $("targetFac").value = "100"; $("targetPh").value = "5.50"; $("saltBenchmark").value = "manual";
    const chemistryBefore = model();
    document.querySelector('[data-benchmark="market"]').click();
    const market = model();
    const expectedSaltFactor = Math.pow(GENERATOR_SALT_G_L / MARKET_SALT_G_L, SALT_CONDUCTIVITY_EXPONENT);
    check("market preset", market.benchmark === "market" && near(market.targetPh, 5.35) && near(market.benchmarkRate, 0.6));
    check("experimental salt recipe", near(market.salt, 0.6) && !near(market.salt, chemistryBefore.salt) && near(market.vinegar, chemistryBefore.vinegar));
    check("low-salt time estimated", near(market.saltTimeFactor, expectedSaltFactor) && near(market.time, 8 * expectedSaltFactor) && $("saltTimerOut").textContent === `${expectedSaltFactor.toFixed(2)}×` && evidenceText(market).includes("constant-voltage-like"));
    check("experimental program gate", !market.official && market.program.note.includes("manual stop"));
    check("no wattage correction", market.outputWatts === null);

    $("saltBenchmark").value = "chloe"; $("volume").value = "500"; $("targetFac").value = "400"; $("targetPh").value = "4.5"; update();
    const chloe = model();
    check("Amazon review source record", chloe.reviewDerived && near(chloe.volume, 500) && near(chloe.targetFac, 400) && near(chloe.salt, 3) && near(chloe.vinegar, 1.25) && near(chloe.reviewClaimTime, 15) && near(chloe.reviewAnchor.fac, 400));
    check("Chloe observed-rate calibration", near(chloe.reviewCalibrationFacRate, 20) && near(chloe.reviewCalibrationMassRate, 5) && near(chloe.time, 40));
    $("volume").value = "250"; $("targetFac").value = "300"; update();
    const chloeLocal = model();
    check("User calibration identity", chloeLocal.reviewDerived && near(chloeLocal.salt, 1.5) && near(chloeLocal.vinegar, 0.625) && near(chloeLocal.time, 15) && near(chloeLocal.reviewClaimTime, 5.625));
    $("volume").value = "1000"; $("targetFac").value = "400";
    const chloeFull = model();
    check("Chloe calibrated volume scaling", chloeFull.reviewDerived && near(chloeFull.salt, 6) && near(chloeFull.vinegar, 2.5) && near(chloeFull.time, 80) && chloeFull.program.note.includes("Amazon/Chloe"));
    $("saltBenchmark").value = "market"; $("volume").value = "1000"; $("targetFac").value = "100"; $("targetPh").value = "5.35"; update();

    $("measuredFac").value = ""; $("measuredPh").value = ""; $("facMethod").value = ""; $("phMethod").value = "";
    check("both missing", state().code === "missing-both");
    $("measuredFac").value = "100";
    check("one missing", state().code === "missing-one");
    $("measuredPh").value = "3"; $("facMethod").value = "fit"; $("phMethod").value = "meter";
    check("pH stop", state().code === "ph-stop");
    $("measuredPh").value = "5.35";
    check("paired preferred", state().code === "preferred");
    check("report identity", report().includes("Generator NaCl: 0.60 g") && report().includes(`Salt-time factor: ${expectedSaltFactor.toFixed(2)}×`) && report().includes("Power correction: none") && report().includes(`Planned time: ${(8 * expectedSaltFactor).toFixed(2)} minutes`));

    Object.entries(saved).forEach(([id, value]) => { $(id).value = value; });
    update();
    window.hoclTestFailures = checks.filter(([, pass]) => !pass).map(([name]) => name);
    return window.hoclTestFailures.length === 0;
  }

  window.runHocRecipeGuideTests = test;
  window.exportHocCalibrationReport = report;
  window.hoclRecipeModel = { baseTime, deviceProgram, model };

  ["volume", "targetFac", "targetPh", "waterPh"].forEach(id => $(id).addEventListener("input", update));
  document.querySelectorAll("[data-fac]").forEach(button => button.addEventListener("click", () => { $("targetFac").value = button.dataset.fac; update(); }));
  document.querySelectorAll("[data-ph]").forEach(button => button.addEventListener("click", () => { $("targetPh").value = button.dataset.ph; update(); }));
  document.querySelectorAll("[data-benchmark]").forEach(button => button.addEventListener("click", () => {
    const benchmark = button.dataset.benchmark;
    $("saltBenchmark").value = benchmark;
    if (benchmark === "chloe") {
      $("volume").value = String(CHLOE_USER_CALIBRATION.volume);
      $("targetFac").value = String(CHLOE_USER_CALIBRATION.fac);
      $("targetPh").value = String(CHLOE_USER_CALIBRATION.ph);
    } else {
      $("targetPh").value = benchmark === "market" ? "5.35" : "4.77";
    }
    update();
  }));
  ["measuredFac", "measuredPh", "batchId"].forEach(id => $(id).addEventListener("input", () => renderDecision(model())));
  ["facMethod", "phMethod", "repeatCount"].forEach(id => $(id).addEventListener("change", () => renderDecision(model())));
  $("copy").addEventListener("click", copyReport);
  $("download").addEventListener("click", download);

  update();
  if (new URLSearchParams(location.search).get("test") === "1") {
    $("selfTest").hidden = false;
    const passed = test();
    $("selfTest").textContent = passed
      ? "Self-test passed: observed-rate default, proportional 250 mL volume scaling, FAC scaling, published anchors, 500 mL validation, documented-recipe identity, experimental 0.60 g/L salt scaling, Amazon/Chloe source context, program feasibility, joint QC states, and report export."
      : `Self-test failed: ${window.hoclTestFailures.join(", ")}.`;
  }
})();
