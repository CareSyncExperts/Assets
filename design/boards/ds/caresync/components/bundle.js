/* @ds-bundle: {"format":4,"namespace":"CareSync","components":[{"name":"Button"},{"name":"IconButton"},{"name":"Icon"},{"name":"Input"},{"name":"Textarea"},{"name":"Select"},{"name":"Checkbox"},{"name":"RadioGroup"},{"name":"Switch"},{"name":"DatePicker"},{"name":"FileUpload"},{"name":"StatusBadge"},{"name":"Alert"},{"name":"Toast"},{"name":"Skeleton"},{"name":"Card"},{"name":"KpiCard"},{"name":"DataTable"},{"name":"Tabs"},{"name":"Breadcrumbs"},{"name":"SideNav"},{"name":"TopBar"},{"name":"Dropdown"},{"name":"Tooltip"},{"name":"Dialog"},{"name":"AlertDialog"},{"name":"Sheet"},{"name":"EmptyState"},{"name":"ErrorState"},{"name":"PermissionDenied"},{"name":"SignedBanner"},{"name":"ArchivedBanner"},{"name":"AuditTimeline"},{"name":"VersionCompare"},{"name":"UnsavedChanges"},{"name":"BulkConfirm"},{"name":"PatternRecordPreview"},{"name":"PatternEvidenceRegister"},{"name":"PatternGuidedWizard"},{"name":"PatternDecisionQueue"}]} */
(function () {
  'use strict';
  var React = window.React;
  var h = React.createElement;
  var useState = React.useState, useRef = React.useRef, useEffect = React.useEffect, useId = React.useId, Fragment = React.Fragment;
  var ICONS = {"check":[["path",{"d":"M20 6 9 17l-5-5"}]],"x":[["path",{"d":"M18 6 6 18"}],["path",{"d":"m6 6 12 12"}]],"chevron-down":[["path",{"d":"m6 9 6 6 6-6"}]],"chevron-up":[["path",{"d":"m18 15-6-6-6 6"}]],"chevron-right":[["path",{"d":"m9 18 6-6-6-6"}]],"chevron-left":[["path",{"d":"m15 18-6-6 6-6"}]],"chevrons-up-down":[["path",{"d":"m7 15 5 5 5-5"}],["path",{"d":"m7 9 5-5 5 5"}]],"arrow-up":[["path",{"d":"m5 12 7-7 7 7"}],["path",{"d":"M12 19V5"}]],"arrow-down":[["path",{"d":"M12 5v14"}],["path",{"d":"m19 12-7 7-7-7"}]],"search":[["path",{"d":"m21 21-4.34-4.34"}],["circle",{"cx":"11","cy":"11","r":"8"}]],"funnel":[["path",{"d":"M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z"}]],"plus":[["path",{"d":"M5 12h14"}],["path",{"d":"M12 5v14"}]],"upload":[["path",{"d":"M12 3v12"}],["path",{"d":"m17 8-5-5-5 5"}],["path",{"d":"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"}]],"file-text":[["path",{"d":"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"}],["path",{"d":"M14 2v5a1 1 0 0 0 1 1h5"}],["path",{"d":"M10 9H8"}],["path",{"d":"M16 13H8"}],["path",{"d":"M16 17H8"}]],"calendar":[["path",{"d":"M8 2v3"}],["path",{"d":"M16 2v3"}],["rect",{"x":"3","y":"3","width":"18","height":"18","rx":"2"}],["path",{"d":"M3 9h18"}]],"info":[["circle",{"cx":"12","cy":"12","r":"10"}],["path",{"d":"M12 16v-4"}],["path",{"d":"M12 8h.01"}]],"circle-check":[["circle",{"cx":"12","cy":"12","r":"10"}],["path",{"d":"m16 9-5.5 5.5L8 12"}]],"triangle-alert":[["path",{"d":"m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"}],["path",{"d":"M12 9v4"}],["path",{"d":"M12 17h.01"}]],"circle-alert":[["circle",{"cx":"12","cy":"12","r":"10"}],["line",{"x1":"12","x2":"12","y1":"8","y2":"12"}],["line",{"x1":"12","x2":"12.01","y1":"16","y2":"16"}]],"octagon-alert":[["path",{"d":"M12 16h.01"}],["path",{"d":"M12 8v4"}],["path",{"d":"M15.312 2a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586l-4.688-4.688A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2z"}]],"lock":[["rect",{"width":"18","height":"11","x":"3","y":"11","rx":"2","ry":"2"}],["path",{"d":"M7 11V7a5 5 0 0 1 10 0v4"}]],"archive":[["rect",{"width":"20","height":"5","x":"2","y":"3","rx":"1"}],["path",{"d":"M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8"}],["path",{"d":"M10 12h4"}]],"pencil-line":[["path",{"d":"M13 21h8"}],["path",{"d":"m15 5 4 4"}],["path",{"d":"M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"}]],"history":[["path",{"d":"M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"}],["path",{"d":"M3 3v5h5"}],["path",{"d":"M12 7v5l4 2"}]],"git-compare":[["circle",{"cx":"18","cy":"18","r":"3"}],["circle",{"cx":"6","cy":"6","r":"3"}],["path",{"d":"M13 6h3a2 2 0 0 1 2 2v7"}],["path",{"d":"M11 18H8a2 2 0 0 1-2-2V9"}]],"users":[["path",{"d":"M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"}],["path",{"d":"M16 3.128a4 4 0 0 1 0 7.744"}],["path",{"d":"M22 21v-2a4 4 0 0 0-3-3.87"}],["circle",{"cx":"9","cy":"7","r":"4"}]],"user":[["path",{"d":"M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"}],["circle",{"cx":"12","cy":"7","r":"4"}]],"layout-dashboard":[["rect",{"width":"7","height":"9","x":"3","y":"3","rx":"1"}],["rect",{"width":"7","height":"5","x":"14","y":"3","rx":"1"}],["rect",{"width":"7","height":"9","x":"14","y":"12","rx":"1"}],["rect",{"width":"7","height":"5","x":"3","y":"16","rx":"1"}]],"file-check":[["path",{"d":"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z"}],["path",{"d":"M14 2v5a1 1 0 0 0 1 1h5"}],["path",{"d":"m9 15 2 2 4-4"}]],"shield-check":[["path",{"d":"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"}],["path",{"d":"m9 12 2 2 4-4"}]],"settings":[["path",{"d":"M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915"}],["circle",{"cx":"12","cy":"12","r":"3"}]],"bell":[["path",{"d":"M10.268 21a2 2 0 0 0 3.464 0"}],["path",{"d":"M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326"}]],"menu":[["path",{"d":"M4 5h16"}],["path",{"d":"M4 12h16"}],["path",{"d":"M4 19h16"}]],"log-out":[["path",{"d":"m16 17 5-5-5-5"}],["path",{"d":"M21 12H9"}],["path",{"d":"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}]],"ellipsis":[["circle",{"cx":"12","cy":"12","r":"1"}],["circle",{"cx":"19","cy":"12","r":"1"}],["circle",{"cx":"5","cy":"12","r":"1"}]],"trash-2":[["path",{"d":"M10 11v6"}],["path",{"d":"M14 11v6"}],["path",{"d":"M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"}],["path",{"d":"M3 6h18"}],["path",{"d":"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"}]],"download":[["path",{"d":"M12 15V3"}],["path",{"d":"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"}],["path",{"d":"m7 10 5 5 5-5"}]],"eye":[["path",{"d":"M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"}],["circle",{"cx":"12","cy":"12","r":"3"}]],"clipboard-list":[["rect",{"width":"8","height":"4","x":"8","y":"2","rx":"1","ry":"1"}],["path",{"d":"M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"}],["path",{"d":"M12 11h4"}],["path",{"d":"M12 16h4"}],["path",{"d":"M8 11h.01"}],["path",{"d":"M8 16h.01"}]],"graduation-cap":[["path",{"d":"M21.42 10.922a1 1 0 0 0-.019-1.838L12.83 5.18a2 2 0 0 0-1.66 0L2.6 9.08a1 1 0 0 0 0 1.832l8.57 3.908a2 2 0 0 0 1.66 0z"}],["path",{"d":"M22 10v6"}],["path",{"d":"M6 12.5V16a6 3 0 0 0 12 0v-3.5"}]],"inbox":[["polyline",{"points":"22 12 16 12 14 15 10 15 8 12 2 12"}],["path",{"d":"M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"}]],"refresh-cw":[["path",{"d":"M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"}],["path",{"d":"M21 3v5h-5"}],["path",{"d":"M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"}],["path",{"d":"M8 16H3v5"}]],"loader-circle":[["path",{"d":"M21 12a9 9 0 1 1-6.219-8.56"}]],"circle-help":[["circle",{"cx":"12","cy":"12","r":"10"}],["path",{"d":"M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"}],["path",{"d":"M12 17h.01"}]],"building-2":[["path",{"d":"M10 12h4"}],["path",{"d":"M10 8h4"}],["path",{"d":"M14 21v-3a2 2 0 0 0-4 0v3"}],["path",{"d":"M6 10H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-2"}],["path",{"d":"M6 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v16"}]],"calendar-check":[["path",{"d":"M8 2v3"}],["path",{"d":"M16 2v3"}],["rect",{"x":"3","y":"3","width":"18","height":"18","rx":"2"}],["path",{"d":"M3 9h18"}],["path",{"d":"m9 15 2 2 4-4"}]],"signature":[["path",{"d":"m21 17-2.156-1.868A.5.5 0 0 0 18 15.5v.5a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1c0-2.545-3.991-3.97-8.5-4a1 1 0 0 0 0 5c4.153 0 4.745-11.295 5.708-13.5a2.5 2.5 0 1 1 3.31 3.284"}],["path",{"d":"M3 21h18"}]],"save":[["path",{"d":"M15.2 3a2 2 0 0 1 1.4.6l3.8 3.8a2 2 0 0 1 .6 1.4V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2z"}],["path",{"d":"M17 21v-7a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v7"}],["path",{"d":"M7 3v4a1 1 0 0 0 1 1h7"}]],"archive-restore":[["rect",{"width":"20","height":"5","x":"2","y":"3","rx":"1"}],["path",{"d":"M4 8v11a2 2 0 0 0 2 2h2"}],["path",{"d":"M20 8v11a2 2 0 0 1-2 2h-2"}],["path",{"d":"m9 15 3-3 3 3"}],["path",{"d":"M12 12v9"}]],"shield-alert":[["path",{"d":"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"}],["path",{"d":"M12 8v4"}],["path",{"d":"M12 16h.01"}]],"circle-x":[["circle",{"cx":"12","cy":"12","r":"10"}],["path",{"d":"m15 9-6 6"}],["path",{"d":"m9 9 6 6"}]],"trending-up":[["path",{"d":"M16 7h6v6"}],["path",{"d":"m22 7-8.5 8.5-5-5L2 17"}]],"trending-down":[["path",{"d":"M16 17h6v-6"}],["path",{"d":"m22 17-8.5-8.5-5 5L2 7"}]],"minus":[["path",{"d":"M5 12h14"}]],"clock":[["circle",{"cx":"12","cy":"12","r":"10"}],["path",{"d":"M12 6v6l4 2"}]],"file-clock":[["path",{"d":"M16 22h2a2 2 0 0 0 2-2V8a2.4 2.4 0 0 0-.706-1.706l-3.588-3.588A2.4 2.4 0 0 0 14 2H6a2 2 0 0 0-2 2v2.85"}],["path",{"d":"M14 2v5a1 1 0 0 0 1 1h5"}],["path",{"d":"M8 14v2.2l1.6 1"}],["circle",{"cx":"8","cy":"16","r":"6"}]],"list-checks":[["path",{"d":"M13 5h8"}],["path",{"d":"M13 12h8"}],["path",{"d":"M13 19h8"}],["path",{"d":"m3 17 2 2 4-4"}],["path",{"d":"m3 7 2 2 4-4"}]],"external-link":[["path",{"d":"M15 3h6v6"}],["path",{"d":"M10 14 21 3"}],["path",{"d":"M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"}]],"link":[["path",{"d":"M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"}],["path",{"d":"M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"}]],"eye-off":[["path",{"d":"M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49"}],["path",{"d":"M14.084 14.158a3 3 0 0 1-4.242-4.242"}],["path",{"d":"M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143"}],["path",{"d":"m2 2 20 20"}]],"rotate-ccw":[["path",{"d":"M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"}],["path",{"d":"M3 3v5h5"}]]};

  function cx() {
    var out = [];
    for (var i = 0; i < arguments.length; i++) if (arguments[i]) out.push(arguments[i]);
    return out.join(' ');
  }
  function omit(obj, keys) {
    var o = {};
    for (var k in obj) if (Object.prototype.hasOwnProperty.call(obj, k) && keys.indexOf(k) < 0) o[k] = obj[k];
    return o;
  }
  var FOCUSABLE = 'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])';

  var STATUS_ICON = { success: 'circle-check', warning: 'triangle-alert', error: 'octagon-alert', info: 'info', neutral: 'circle-help', brand: 'shield-check' };

  /* Icon: one component, the glyph swapped by name */
  function Icon(p) {
    var size = p.size || 20;
    var def = ICONS[p.name];
    if (!def) return null;
    var a11y = p.label ? { role: 'img', 'aria-label': p.label } : { 'aria-hidden': 'true', focusable: 'false' };
    return h('svg', Object.assign({ className: cx('cs-icon', p.className), width: size, height: size, viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor', strokeWidth: 2, strokeLinecap: 'round', strokeLinejoin: 'round' }, a11y),
      def.map(function (el, i) { return h(el[0], Object.assign({ key: i }, el[1])); }));
  }
  Icon.names = Object.keys(ICONS);

  /* Button */
  function Button(p) {
    var variant = p.variant || 'primary', size = p.size || 'default';
    var rest = omit(p, ['variant', 'size', 'loading', 'loadingLabel', 'iconStart', 'iconEnd', 'demoState', 'pill', 'block', 'className', 'children', 'type']);
    var iconSize = size === 'small' ? 16 : 20;
    var busy = !!p.loading;
    return h('button', Object.assign({
      type: p.type || 'button',
      className: cx('cs-btn', 'cs-btn--' + variant, size !== 'default' && 'cs-btn--' + size, p.pill && 'cs-btn--pill', p.block && 'cs-btn--block', p.demoState && 'cs-is-' + p.demoState, p.className),
      'aria-busy': busy ? 'true' : undefined,
      'aria-disabled': busy ? 'true' : undefined,
      onClick: busy ? function (e) { e.preventDefault(); } : p.onClick
    }, rest),
      !busy && p.iconStart ? h(Icon, { name: p.iconStart, size: iconSize }) : null,
      h('span', null, busy ? (p.loadingLabel || 'Saving') : p.children),
      !busy && p.iconEnd ? h(Icon, { name: p.iconEnd, size: iconSize }) : null
    );
  }

  /* IconButton: label is required and becomes the accessible name and tooltip */
  function IconButton(p) {
    var rest = omit(p, ['icon', 'label', 'variant', 'size', 'className', 'tooltip']);
    var btn = h('button', Object.assign({ type: 'button', 'aria-label': p.label, className: cx('cs-iconbtn', p.variant && 'cs-iconbtn--' + p.variant, p.size === 'small' && 'cs-iconbtn--small', p.className) }, rest),
      h(Icon, { name: p.icon, size: p.size === 'small' ? 16 : 20 }));
    return p.tooltip === false ? btn : h(Tooltip, { content: p.label, labelOnly: true }, btn);
  }

  /* Field plumbing shared by text controls */
  function useFieldIds(id) {
    var auto = useId();
    var base = id || 'cs' + auto.replace(/:/g, '');
    return { control: base, hint: base + '-hint', error: base + '-error' };
  }
  function FieldShell(p) {
    return h('div', { className: cx('cs-field', p.className) },
      h('label', { className: 'cs-label', htmlFor: p.ids.control }, p.label, p.required ? h('span', { className: 'cs-req' }, ' (required)') : (p.optional ? h('span', { className: 'cs-req' }, ' (optional)') : null)),
      p.hint ? h('p', { className: 'cs-hint', id: p.ids.hint }, p.hint) : null,
      p.error ? h('p', { className: 'cs-error', id: p.ids.error }, h(Icon, { name: 'circle-alert', size: 16 }), h('span', null, h('span', { className: 'cs-sr' }, 'Error: '), p.error)) : null,
      p.children,
      p.after || null
    );
  }
  function describedBy(p, ids) {
    var list = [];
    if (p.hint) list.push(ids.hint);
    if (p.error) list.push(ids.error);
    return list.length ? list.join(' ') : undefined;
  }
  var FIELD_KEYS = ['label', 'hint', 'error', 'required', 'optional', 'className', 'size', 'id'];

  function Input(p) {
    var ids = useFieldIds(p.id);
    var rest = omit(p, FIELD_KEYS);
    return h(FieldShell, { ids: ids, label: p.label, hint: p.hint, error: p.error, required: p.required, optional: p.optional, className: p.className },
      h('input', Object.assign({ id: ids.control, className: cx('cs-control', p.size === 'small' && 'cs-control--small'), 'aria-describedby': describedBy(p, ids), 'aria-invalid': p.error ? 'true' : undefined, required: p.required }, rest)));
  }

  function Textarea(p) {
    var ids = useFieldIds(p.id);
    var init = p.defaultValue || '';
    var s = useState(init.length); var count = s[0], setCount = s[1];
    var rest = omit(p, FIELD_KEYS.concat(['maxLength', 'onChange']));
    return h(FieldShell, {
      ids: ids, label: p.label, hint: p.hint, error: p.error, required: p.required, optional: p.optional, className: p.className,
      after: p.maxLength ? h('span', { className: 'cs-count', 'aria-live': 'polite' }, count + ' of ' + p.maxLength + ' characters') : null
    },
      h('textarea', Object.assign({ id: ids.control, className: 'cs-control', maxLength: p.maxLength, 'aria-describedby': describedBy(p, ids), 'aria-invalid': p.error ? 'true' : undefined, required: p.required,
        onChange: function (e) { setCount(e.target.value.length); if (p.onChange) p.onChange(e); } }, rest)));
  }

  function Select(p) {
    var ids = useFieldIds(p.id);
    var rest = omit(p, FIELD_KEYS.concat(['options', 'placeholder']));
    return h(FieldShell, { ids: ids, label: p.label, hint: p.hint, error: p.error, required: p.required, optional: p.optional, className: p.className },
      h('div', { className: 'cs-select-wrap' },
        h('select', Object.assign({ id: ids.control, className: 'cs-control', 'aria-describedby': describedBy(p, ids), 'aria-invalid': p.error ? 'true' : undefined, required: p.required }, rest),
          p.placeholder ? h('option', { value: '' }, p.placeholder) : null,
          (p.options || []).map(function (o) { var v = typeof o === 'string' ? { value: o, label: o } : o; return h('option', { key: v.value, value: v.value, disabled: v.disabled }, v.label); })),
        h(Icon, { name: 'chevron-down', size: 20 })));
  }

  function DatePicker(p) {
    var ids = useFieldIds(p.id);
    var rest = omit(p, FIELD_KEYS);
    return h(FieldShell, { ids: ids, label: p.label, hint: p.hint || 'Type the date or use the calendar. For example, 27/03/2026.', error: p.error, required: p.required, optional: p.optional, className: p.className },
      h('input', Object.assign({ id: ids.control, type: 'date', className: 'cs-control', 'aria-describedby': describedBy(Object.assign({}, p, { hint: true }), ids), 'aria-invalid': p.error ? 'true' : undefined, required: p.required }, rest)));
  }

  function Checkbox(p) {
    var ids = useFieldIds(p.id);
    var ref = useRef(null);
    useEffect(function () { if (ref.current) ref.current.indeterminate = !!p.indeterminate; }, [p.indeterminate]);
    var rest = omit(p, ['label', 'hint', 'error', 'indeterminate', 'className', 'id', 'hideLabel']);
    return h('div', { className: cx('cs-field', p.className) },
      h('label', { className: 'cs-check', htmlFor: ids.control },
        h('input', Object.assign({ ref: ref, id: ids.control, type: 'checkbox', 'aria-describedby': describedBy(p, ids), 'aria-invalid': p.error ? 'true' : undefined }, rest)),
        h('span', { className: 'cs-check-box', 'aria-hidden': 'true' }, h(Icon, { name: p.indeterminate ? 'minus' : 'check', size: 14 })),
        h('span', { className: cx('cs-check-text', p.hideLabel && 'cs-sr') }, h('span', null, p.label), p.hint ? h('span', { className: 'cs-hint', id: ids.hint }, p.hint) : null)),
      p.error ? h('p', { className: 'cs-error', id: ids.error }, h(Icon, { name: 'circle-alert', size: 16 }), h('span', null, p.error)) : null);
  }

  function RadioGroup(p) {
    var ids = useFieldIds(p.id);
    var name = p.name || ids.control;
    return h('fieldset', { className: cx('cs-fieldset', p.className), 'aria-describedby': describedBy(p, ids), 'aria-invalid': p.error ? 'true' : undefined },
      h('legend', { className: 'cs-label' }, p.legend, p.required ? h('span', { className: 'cs-req' }, ' (required)') : null),
      p.hint ? h('p', { className: 'cs-hint', id: ids.hint }, p.hint) : null,
      p.error ? h('p', { className: 'cs-error', id: ids.error }, h(Icon, { name: 'circle-alert', size: 16 }), h('span', null, p.error)) : null,
      h('div', { style: { display: 'grid', gap: 0 } }, (p.options || []).map(function (o, i) {
        var oid = ids.control + '-' + i;
        return h('label', { key: o.value, className: 'cs-check cs-check--radio', htmlFor: oid },
          h('input', { id: oid, type: 'radio', name: name, value: o.value, defaultChecked: p.defaultValue === o.value, disabled: o.disabled, required: p.required, 'aria-invalid': p.error ? 'true' : undefined, onChange: p.onChange }),
          h('span', { className: 'cs-check-box', 'aria-hidden': 'true' }),
          h('span', { className: 'cs-check-text' }, h('span', null, o.label), o.hint ? h('span', { className: 'cs-hint' }, o.hint) : null));
      })));
  }

  function Switch(p) {
    var ids = useFieldIds(p.id);
    var controlled = p.checked !== undefined;
    var s = useState(!!p.defaultChecked); var on = controlled ? p.checked : s[0];
    function toggle() { if (p.disabled) return; if (!controlled) s[1](!on); if (p.onChange) p.onChange(!on); }
    return h('div', { className: cx('cs-switch-row', p.className) },
      h('div', { className: 'cs-check-text' }, h('span', { className: 'cs-label', id: ids.control + '-label' }, p.label), p.hint ? h('span', { className: 'cs-hint', id: ids.hint }, p.hint) : null),
      h('span', { className: 'cs-switch-ctrl' },
        h('span', { className: 'cs-switch-state', 'aria-hidden': 'true' }, on ? 'On' : 'Off'),
        h('button', { type: 'button', role: 'switch', id: ids.control, className: 'cs-switch', 'aria-checked': on ? 'true' : 'false', 'aria-labelledby': ids.control + '-label', 'aria-describedby': p.hint ? ids.hint : undefined, disabled: p.disabled, onClick: toggle })));
  }

  function formatBytes(n) { return n > 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB'; }
  function FileUpload(p) {
    var ids = useFieldIds(p.id);
    var inputRef = useRef(null);
    var s = useState(p.files || []); var files = s[0], setFiles = s[1];
    var o = useState(false); var over = o[0], setOver = o[1];
    function add(list) {
      var next = files.slice();
      for (var i = 0; i < list.length; i++) next.push({ name: list[i].name, size: list[i].size, status: 'ready' });
      setFiles(next); if (p.onFiles) p.onFiles(list);
    }
    return h('div', { className: cx('cs-field', p.className) },
      h('span', { className: 'cs-label', id: ids.control + '-label' }, p.label, p.required ? h('span', { className: 'cs-req' }, ' (required)') : null),
      p.hint ? h('p', { className: 'cs-hint', id: ids.hint }, p.hint) : null,
      p.error ? h('p', { className: 'cs-error', id: ids.error }, h(Icon, { name: 'circle-alert', size: 16 }), h('span', null, p.error)) : null,
      h('div', {
        className: cx('cs-drop', over && 'cs-is-over'),
        onDragOver: function (e) { e.preventDefault(); setOver(true); },
        onDragLeave: function () { setOver(false); },
        onDrop: function (e) { e.preventDefault(); setOver(false); add(e.dataTransfer.files); }
      },
        h(Icon, { name: 'upload', size: 24 }),
        h('span', null, 'Drag files here, or'),
        h(Button, { variant: 'secondary', size: 'small', iconStart: 'file-text', 'aria-describedby': describedBy(p, ids), onClick: function () { inputRef.current && inputRef.current.click(); } }, p.buttonLabel || 'Choose files'),
        h('input', { ref: inputRef, id: ids.control, type: 'file', className: 'cs-sr', tabIndex: -1, 'aria-labelledby': ids.control + '-label', accept: p.accept, multiple: p.multiple, onChange: function (e) { add(e.target.files); } })),
      files.length ? h('ul', { className: 'cs-files', 'aria-label': 'Selected files' }, files.map(function (f, i) {
        var uploading = f.status === 'uploading';
        return h('li', { key: f.name + i, className: 'cs-file' },
          uploading ? h(Icon, { name: 'loader-circle', size: 20, className: 'cs-spin' }) : h(Icon, { name: f.status === 'error' ? 'circle-alert' : (f.status === 'done' ? 'circle-check' : 'file-text'), size: 20 }),
          h('div', null,
            h('div', { className: 'cs-file-name' }, f.name),
            h('div', { className: 'cs-file-meta' }, formatBytes(f.size || 0), ' · ',
              uploading ? 'Uploading, ' + (f.progress || 0) + '%' : f.status === 'done' ? 'Uploaded' : f.status === 'error' ? (f.message || 'Upload failed. Try again.') : 'Ready to upload'),
            uploading ? h('div', { className: 'cs-progress', role: 'progressbar', 'aria-label': 'Uploading ' + f.name, 'aria-valuenow': f.progress || 0, 'aria-valuemin': 0, 'aria-valuemax': 100 }, h('span', { style: { width: (f.progress || 0) + '%' } })) : null),
          h(IconButton, { icon: 'x', label: 'Remove ' + f.name, variant: 'neutral', size: 'small', onClick: function () { setFiles(files.filter(function (_, j) { return j !== i; })); } }));
      })) : null);
  }

  /* Status badge: status is always carried by the words, the icon repeats it */
  function StatusBadge(p) {
    var status = p.status || 'neutral';
    var icon = p.icon === false ? null : (p.icon || STATUS_ICON[status]);
    return h('span', { className: cx('cs-badge', 'cs-badge--' + status, p.className) }, icon ? h(Icon, { name: icon, size: 14 }) : null, p.children);
  }

  function Card(p) {
    var Tag = p.as || 'section';
    var auto = useId();
    var tid = p.title ? 'cs' + auto.replace(/:/g, '') + '-title' : undefined;
    return h(Tag, { className: cx('cs-card', p.flush && 'cs-card--flush', p.className), 'aria-labelledby': tid },
      (p.title || p.actions) ? h('div', { className: 'cs-card-head', style: p.flush ? { padding: '20px 24px 0' } : null },
        h('div', null, p.title ? h('h2', { className: 'cs-card-title', id: tid }, p.title) : null, p.description ? h('p', { className: 'cs-card-desc' }, p.description) : null),
        p.actions || null) : null,
      p.children);
  }

  function KpiCard(p) {
    var trendIcon = p.trend === 'up' ? 'trending-up' : p.trend === 'down' ? 'trending-down' : null;
    return h('section', { className: cx('cs-card cs-kpi', p.className), 'aria-label': p.label },
      h('p', { className: 'cs-kpi-label' }, p.icon ? h(Icon, { name: p.icon, size: 20 }) : null, p.label),
      h('p', { className: 'cs-kpi-value' }, p.value),
      (p.change || p.status || p.helper) ? h('div', { className: 'cs-kpi-foot' },
        p.status ? h(StatusBadge, { status: p.status.tone, icon: trendIcon || undefined }, p.status.text) : null,
        p.helper ? h('span', null, p.helper) : null) : null);
  }

  /* DataTable: semantic table, aria-sort, filter, selection, pagination, horizontal scroll region */
  function DataTable(p) {
    var auto = useId(); var base = 'cs' + auto.replace(/:/g, '');
    var cols = p.columns || [];
    var s1 = useState(p.defaultSort || null); var sort = s1[0], setSort = s1[1];
    var s2 = useState(''); var q = s2[0], setQ = s2[1];
    var s3 = useState(p.defaultSelected || []); var sel = s3[0], setSel = s3[1];
    var s4 = useState(0); var page = s4[0], setPage = s4[1];
    var s5 = useState(p.density || 'comfortable'); var density = s5[0], setDensity = s5[1];
    var pageSize = p.pageSize || 5;
    var rowKey = p.rowKey || 'id';
    var rows = (p.rows || []).filter(function (r) {
      if (!q) return true;
      var needle = q.toLowerCase();
      return cols.some(function (c) { var v = r[c.key]; return v != null && String(typeof v === 'object' && v.text ? v.text : v).toLowerCase().indexOf(needle) >= 0; });
    });
    if (sort) {
      rows = rows.slice().sort(function (a, b) {
        var av = a[sort.key], bv = b[sort.key];
        if (av && av.sort !== undefined) { av = av.sort; bv = bv.sort; }
        if (av && typeof av === 'object' && av.text) { av = av.text; bv = bv.text; }
        var r = typeof av === 'number' ? av - bv : String(av).localeCompare(String(bv), 'en-GB');
        return sort.dir === 'ascending' ? r : -r;
      });
    }
    var pages = Math.max(1, Math.ceil(rows.length / pageSize));
    var pg = Math.min(page, pages - 1);
    var view = rows.slice(pg * pageSize, pg * pageSize + pageSize);
    var viewKeys = view.map(function (r) { return r[rowKey]; });
    var allOn = viewKeys.length > 0 && viewKeys.every(function (k) { return sel.indexOf(k) >= 0; });
    var someOn = !allOn && viewKeys.some(function (k) { return sel.indexOf(k) >= 0; });
    function toggleAll() { setSel(allOn ? sel.filter(function (k) { return viewKeys.indexOf(k) < 0; }) : sel.concat(viewKeys.filter(function (k) { return sel.indexOf(k) < 0; }))); }
    function toggle(k) { setSel(sel.indexOf(k) >= 0 ? sel.filter(function (x) { return x !== k; }) : sel.concat([k])); }
    function sortBy(c) {
      var dir = sort && sort.key === c.key && sort.dir === 'ascending' ? 'descending' : 'ascending';
      setSort({ key: c.key, dir: dir }); setPage(0);
    }
    function cell(r, c) {
      var v = r[c.key];
      if (c.render) return c.render(v, r);
      if (v && typeof v === 'object' && v.status) return h(StatusBadge, { status: v.status }, v.text);
      if (v && typeof v === 'object' && 'text' in v) return v.text;
      return v;
    }
    var first = rows.length ? pg * pageSize + 1 : 0, last = Math.min(rows.length, (pg + 1) * pageSize);
    return h('div', { className: cx('cs-table-card', p.className) },
      h('div', { className: 'cs-table-toolbar' },
        h('div', null, h('h2', { className: 'cs-table-caption', id: base + '-cap' }, p.caption), p.description ? h('p', { className: 'cs-card-desc' }, p.description) : null),
        h('div', { className: 'cs-row' },
          p.filterable === false ? null : h('div', { style: { width: 240 } }, h(Input, { label: p.filterLabel || 'Filter rows', size: 'small', type: 'search', value: q, onChange: function (e) { setQ(e.target.value); setPage(0); } })),
          p.densityToggle === false ? null : h('div', { style: { alignSelf: 'flex-end' } }, h(Button, { variant: 'secondary', size: 'small', 'aria-pressed': density === 'compact' ? 'true' : 'false', onClick: function () { setDensity(density === 'compact' ? 'comfortable' : 'compact'); } }, 'Compact rows')))),
      p.selectable && sel.length ? h('div', { className: 'cs-table-bulk', role: 'status' }, h('span', null, sel.length + (sel.length === 1 ? ' row selected' : ' rows selected')), p.bulkActions ? p.bulkActions(sel) : null, h(Button, { variant: 'ghost', size: 'small', onClick: function () { setSel([]); } }, 'Clear selection')) : h('div', { role: 'status', className: 'cs-sr' }, q ? rows.length + ' matching rows' : ''),
      h('div', { className: 'cs-scroll', role: 'region', 'aria-labelledby': base + '-cap', tabIndex: 0 },
        h('table', { className: cx('cs-table', density === 'compact' && 'cs-table--compact') },
          h('caption', { className: 'cs-sr' }, p.caption, sort ? ', sorted by ' + (cols.filter(function (c) { return c.key === sort.key; })[0] || {}).label + ' ' + sort.dir : ''),
          h('thead', null, h('tr', null,
            p.selectable ? h('th', { scope: 'col', className: 'cs-sel' }, h(Checkbox, { label: 'Select all rows on this page', hideLabel: true, checked: allOn, indeterminate: someOn, onChange: toggleAll })) : null,
            cols.map(function (c) {
              var active = sort && sort.key === c.key;
              return h('th', { key: c.key, scope: 'col', className: c.align === 'end' ? 'cs-num' : undefined, 'aria-sort': c.sortable ? (active ? sort.dir : 'none') : undefined, style: c.width ? { width: c.width } : undefined },
                c.sortable ? h('button', { type: 'button', className: 'cs-th-btn', onClick: function () { sortBy(c); } }, c.label, h(Icon, { name: active ? (sort.dir === 'ascending' ? 'arrow-up' : 'arrow-down') : 'chevrons-up-down', size: 16 })) : c.label);
            }))),
          h('tbody', null, view.length ? view.map(function (r) {
            var k = r[rowKey]; var on = sel.indexOf(k) >= 0;
            return h('tr', { key: k, 'aria-selected': p.selectable ? (on ? 'true' : 'false') : undefined },
              p.selectable ? h('td', { className: 'cs-sel' }, h(Checkbox, { label: 'Select ' + (r[cols[0].key] && r[cols[0].key].text || r[cols[0].key]), hideLabel: true, checked: on, onChange: function () { toggle(k); } })) : null,
              cols.map(function (c, i) {
                var Tag = i === 0 ? 'th' : 'td';
                return h(Tag, { key: c.key, scope: i === 0 ? 'row' : undefined, className: cx(c.align === 'end' && 'cs-num', i === 0 && 'cs-td-strong'), style: i === 0 ? { textAlign: 'left', fontWeight: 500, color: 'var(--cs-text-primary)', background: 'transparent', fontSize: 'inherit' } : undefined }, cell(r, c));
              }));
          }) : h('tr', null, h('td', { colSpan: cols.length + (p.selectable ? 1 : 0), className: 'cs-table-empty' }, p.emptyText || 'No rows match your filter. Clear the filter to see all rows.'))))),
      h('div', { className: 'cs-table-foot' },
        h('span', null, rows.length ? 'Showing ' + first + ' to ' + last + ' of ' + rows.length : 'No rows'),
        h('nav', { className: 'cs-row', 'aria-label': (p.caption || 'Table') + ' pagination' },
          h(Button, { variant: 'secondary', size: 'small', iconStart: 'chevron-left', disabled: pg === 0, onClick: function () { setPage(pg - 1); } }, 'Previous'),
          h('span', { 'aria-live': 'polite' }, 'Page ' + (pg + 1) + ' of ' + pages),
          h(Button, { variant: 'secondary', size: 'small', iconEnd: 'chevron-right', disabled: pg >= pages - 1, onClick: function () { setPage(pg + 1); } }, 'Next'))));
  }

  /* Tabs: roving tabindex, arrow keys, Home and End */
  function Tabs(p) {
    var auto = useId(); var base = 'cs' + auto.replace(/:/g, '');
    var tabs = p.tabs || [];
    var s = useState(p.defaultTab || (tabs[0] && tabs[0].id)); var cur = s[0], setCur = s[1];
    var refs = useRef({});
    function onKey(e, i) {
      var n = tabs.length, next = null;
      if (e.key === 'ArrowRight') next = (i + 1) % n;
      else if (e.key === 'ArrowLeft') next = (i - 1 + n) % n;
      else if (e.key === 'Home') next = 0;
      else if (e.key === 'End') next = n - 1;
      if (next !== null) { e.preventDefault(); setCur(tabs[next].id); refs.current[tabs[next].id].focus(); }
    }
    return h('div', { className: p.className },
      h('div', { role: 'tablist', 'aria-label': p.label, className: 'cs-tablist' }, tabs.map(function (t, i) {
        var on = t.id === cur;
        return h('button', { key: t.id, ref: function (el) { refs.current[t.id] = el; }, type: 'button', role: 'tab', id: base + '-tab-' + t.id, 'aria-selected': on ? 'true' : 'false', 'aria-controls': base + '-panel-' + t.id, tabIndex: on ? 0 : -1, className: 'cs-tab', onClick: function () { setCur(t.id); }, onKeyDown: function (e) { onKey(e, i); } },
          t.label, t.count != null ? h('span', { className: 'cs-tab-count' }, t.count) : null);
      })),
      tabs.map(function (t) {
        return h('div', { key: t.id, role: 'tabpanel', id: base + '-panel-' + t.id, 'aria-labelledby': base + '-tab-' + t.id, hidden: t.id !== cur, tabIndex: 0, className: 'cs-tabpanel' }, t.content);
      }));
  }

  function Breadcrumbs(p) {
    var items = p.items || [];
    return h('nav', { className: 'cs-crumbs', 'aria-label': 'Breadcrumb' }, h('ol', null, items.map(function (it, i) {
      var last = i === items.length - 1;
      return h('li', { key: i }, i > 0 ? h(Icon, { name: 'chevron-right', size: 16 }) : null,
        last ? h('span', { 'aria-current': 'page' }, it.label) : h('a', { href: it.href || '#' }, it.label));
    })));
  }

  function SideNav(p) {
    return h('nav', { className: cx('cs-sidenav', p.className), 'aria-label': p.label || 'Main' },
      p.logo ? h('div', { className: 'cs-sidenav-brand' }, h('span', { style: { display: 'grid', gap: 8 } }, p.logo, p.productSub ? h('small', null, p.productSub) : null))
        : p.product ? h('div', { className: 'cs-sidenav-brand' }, h('span', null, p.product, p.productSub ? h('small', null, p.productSub) : null)) : null,
      (p.sections || [{ items: p.items || [] }]).map(function (sec, si) {
        var hid = sec.heading ? 'cs-navh-' + si : undefined;
        return h('div', { key: si, className: 'cs-nav-section' },
          sec.heading ? h('h2', { className: 'cs-nav-heading', id: hid }, sec.heading) : null,
          h('ul', { className: 'cs-nav-list', 'aria-labelledby': hid }, sec.items.map(function (it) {
            return h('li', { key: it.label }, h('a', { className: 'cs-nav-link', href: it.href || '#', 'aria-current': it.current ? 'page' : undefined },
              it.icon ? h(Icon, { name: it.icon, size: 20 }) : null, h('span', null, it.label), it.badge ? h(StatusBadge, { status: it.badge.status || 'warning' }, it.badge.text) : null));
          })));
      }));
  }

  function TopBar(p) {
    return h('header', { className: cx('cs-topbar', p.compact && 'cs-topbar--compact', p.className) },
      h('span', { className: 'cs-topbar-menu' }, h(IconButton, { icon: 'menu', label: 'Open navigation', variant: 'neutral', 'aria-expanded': p.menuOpen ? 'true' : 'false', onClick: p.onMenu })),
      p.logo ? h('span', { style: { flex: 'none', display: 'inline-flex' } }, p.logo) : null,
      h('div', { style: { minWidth: 0 } }, p.breadcrumbs ? h(Breadcrumbs, { items: p.breadcrumbs }) : null, p.title ? h('p', { className: 'cs-topbar-title' }, p.title) : null),
      h('div', { className: 'cs-topbar-actions' }, p.actions || null,
        h(IconButton, { icon: 'bell', label: p.notifications ? 'Notifications, ' + p.notifications + ' unread' : 'Notifications', variant: 'neutral' }),
        p.user ? h(Dropdown, { align: 'end', trigger: { label: 'Account menu for ' + p.user.name, avatar: p.user.initials }, items: [{ label: 'Profile', icon: 'user' }, { label: 'Settings', icon: 'settings' }, { separator: true }, { label: 'Sign out', icon: 'log-out' }] }) : null));
  }

  /* Dropdown menu: button + role=menu, arrows, Home, End, Escape returns focus */
  function Dropdown(p) {
    var s = useState(false); var open = s[0], setOpen = s[1];
    var auto = useId(); var base = 'cs' + auto.replace(/:/g, '');
    var wrap = useRef(null), trig = useRef(null), menu = useRef(null);
    var items = p.items || [];
    useEffect(function () {
      if (!open) return;
      var first = menu.current && menu.current.querySelector('[role="menuitem"]:not([disabled])');
      if (first) first.focus();
      function outside(e) { if (wrap.current && !wrap.current.contains(e.target)) setOpen(false); }
      document.addEventListener('mousedown', outside);
      return function () { document.removeEventListener('mousedown', outside); };
    }, [open]);
    function close(refocus) { setOpen(false); if (refocus && trig.current) trig.current.focus(); }
    function onKey(e) {
      var list = Array.prototype.slice.call(menu.current.querySelectorAll('[role="menuitem"]:not([disabled])'));
      var i = list.indexOf(document.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); list[(i + 1) % list.length].focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); list[(i - 1 + list.length) % list.length].focus(); }
      else if (e.key === 'Home') { e.preventDefault(); list[0].focus(); }
      else if (e.key === 'End') { e.preventDefault(); list[list.length - 1].focus(); }
      else if (e.key === 'Escape') { e.preventDefault(); close(true); }
      else if (e.key === 'Tab') { setOpen(false); }
    }
    var t = p.trigger || {};
    var trigger = t.avatar
      ? h('button', { ref: trig, type: 'button', className: 'cs-iconbtn', 'aria-label': t.label, 'aria-haspopup': 'menu', 'aria-expanded': open ? 'true' : 'false', 'aria-controls': base + '-menu', onClick: function () { setOpen(!open); } }, h('span', { className: 'cs-avatar', 'aria-hidden': 'true' }, t.avatar))
      : t.icon && !t.text
        ? h('button', { ref: trig, type: 'button', className: 'cs-iconbtn cs-iconbtn--neutral', 'aria-label': t.label, 'aria-haspopup': 'menu', 'aria-expanded': open ? 'true' : 'false', 'aria-controls': base + '-menu', onClick: function () { setOpen(!open); } }, h(Icon, { name: t.icon }))
        : h('button', { ref: trig, type: 'button', className: 'cs-btn cs-btn--secondary', 'aria-haspopup': 'menu', 'aria-expanded': open ? 'true' : 'false', 'aria-controls': base + '-menu', onClick: function () { setOpen(!open); } }, h('span', null, t.text || t.label), h(Icon, { name: 'chevron-down', size: 20 }));
    return h('div', { className: 'cs-dropdown', ref: wrap },
      trigger,
      open ? h('ul', { ref: menu, id: base + '-menu', role: 'menu', 'aria-label': t.label || t.text, className: cx('cs-menu', p.align === 'end' && 'cs-menu--end'), onKeyDown: onKey }, items.map(function (it, i) {
        if (it.separator) return h('li', { key: 'sep' + i, role: 'separator', className: 'cs-menu-sep' });
        return h('li', { key: it.label, role: 'none' }, h('button', { type: 'button', role: 'menuitem', tabIndex: -1, disabled: it.disabled, className: cx('cs-menu-item', it.danger && 'cs-menu-item--danger'), onClick: function () { close(true); if (it.onSelect) it.onSelect(); } }, it.icon ? h(Icon, { name: it.icon, size: 20 }) : null, it.label));
      })) : null);
  }

  /* Tooltip: shows on hover and focus, Escape dismisses, content is supplementary */
  function Tooltip(p) {
    var s = useState(false); var show = s[0], setShow = s[1];
    var auto = useId(); var tid = 'cs' + auto.replace(/:/g, '') + '-tip';
    var child = React.Children.only(p.children);
    useEffect(function () {
      if (!show) return;
      function esc(e) { if (e.key === 'Escape') setShow(false); }
      document.addEventListener('keydown', esc);
      return function () { document.removeEventListener('keydown', esc); };
    }, [show]);
    var extra = p.labelOnly ? {} : { 'aria-describedby': tid };
    return h('span', { className: 'cs-tip-wrap', onMouseEnter: function () { setShow(true); }, onMouseLeave: function () { setShow(false); }, onFocus: function () { setShow(true); }, onBlur: function () { setShow(false); } },
      React.cloneElement(child, extra),
      h('span', { role: 'tooltip', id: tid, className: 'cs-tip', hidden: !(show || p.defaultOpen), 'aria-hidden': p.labelOnly ? 'true' : undefined }, p.content));
  }

  /* Focus trap shared by Dialog, AlertDialog and Sheet */
  function useModal(open, onEscape, panelRef, initialRef) {
    useEffect(function () {
      if (!open) return;
      var prev = document.activeElement;
      var panel = panelRef.current;
      var target = (initialRef && initialRef.current) || panel.querySelector('[data-autofocus]') || panel;
      target.focus();
      function onKey(e) {
        if (e.key === 'Escape') { e.stopPropagation(); onEscape && onEscape(); return; }
        if (e.key !== 'Tab') return;
        var list = Array.prototype.slice.call(panel.querySelectorAll(FOCUSABLE)).filter(function (el) { return el.offsetParent !== null || el === document.activeElement; });
        if (!list.length) { e.preventDefault(); return; }
        var first = list[0], last = list[list.length - 1];
        if (e.shiftKey && (document.activeElement === first || document.activeElement === panel)) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
      panel.addEventListener('keydown', onKey);
      return function () { panel.removeEventListener('keydown', onKey); if (prev && prev.focus) prev.focus(); };
    }, [open]);
  }

  function Dialog(p) {
    var ref = useRef(null);
    var auto = useId(); var base = 'cs' + auto.replace(/:/g, '');
    var modal = !p.inline;
    useModal(modal && p.open, p.onClose, ref);
    if (modal && !p.open) return null;
    var panel = h('div', { ref: ref, role: 'dialog', 'aria-modal': modal ? 'true' : undefined, 'aria-labelledby': base + '-t', 'aria-describedby': p.description ? base + '-d' : undefined, tabIndex: -1, className: cx('cs-dialog', p.inline && 'cs-dialog--inline', p.className) },
      h('div', { className: 'cs-dialog-head' },
        h('div', null, h('h2', { className: 'cs-dialog-title', id: base + '-t' }, p.title), p.description ? h('p', { className: 'cs-dialog-desc', id: base + '-d' }, p.description) : null),
        h(IconButton, { icon: 'x', label: 'Close', variant: 'neutral', tooltip: false, onClick: p.onClose })),
      p.children ? h('div', { className: 'cs-stack' }, p.children) : null,
      p.footer ? h('div', { className: 'cs-dialog-foot' }, p.footer) : null);
    return modal ? h('div', { className: 'cs-overlay', onMouseDown: function (e) { if (e.target === e.currentTarget && p.dismissOnScrim !== false && p.onClose) p.onClose(); } }, panel) : panel;
  }

  function AlertDialog(p) {
    var ref = useRef(null), cancelRef = useRef(null);
    var auto = useId(); var base = 'cs' + auto.replace(/:/g, '');
    var modal = !p.inline;
    useModal(modal && p.open, p.onCancel, ref, cancelRef);
    if (modal && !p.open) return null;
    var tone = p.tone || 'danger';
    var panel = h('div', { ref: ref, role: 'alertdialog', 'aria-modal': modal ? 'true' : undefined, 'aria-labelledby': base + '-t', 'aria-describedby': base + '-d', tabIndex: -1, className: cx('cs-dialog', p.inline && 'cs-dialog--inline') },
      h('div', { style: { display: 'flex', gap: 16, alignItems: 'flex-start' } },
        h('span', { className: cx('cs-alert-icon', tone === 'warning' && 'cs-alert-icon--warning') }, h(Icon, { name: tone === 'warning' ? 'triangle-alert' : 'trash-2', size: 24 })),
        h('div', null, h('h2', { className: 'cs-dialog-title', id: base + '-t' }, p.title), h('div', { className: 'cs-dialog-desc', id: base + '-d' }, p.description))),
      p.children || null,
      h('div', { className: 'cs-dialog-foot' },
        h('button', { ref: cancelRef, type: 'button', className: 'cs-btn cs-btn--secondary', onClick: p.onCancel }, h('span', null, p.cancelLabel || 'Cancel')),
        h(Button, { variant: tone === 'danger' ? 'destructive' : 'primary', onClick: p.onConfirm, loading: p.busy, loadingLabel: p.busyLabel, disabled: p.confirmDisabled }, p.confirmLabel || 'Confirm')));
    return modal ? h('div', { className: 'cs-overlay' }, panel) : panel;
  }

  function Sheet(p) {
    var ref = useRef(null);
    var auto = useId(); var base = 'cs' + auto.replace(/:/g, '');
    var modal = !p.inline;
    useModal(modal && p.open, p.onClose, ref);
    if (modal && !p.open) return null;
    var panel = h('div', { ref: ref, role: 'dialog', 'aria-modal': modal ? 'true' : undefined, 'aria-labelledby': base + '-t', tabIndex: -1, className: cx('cs-sheet', p.inline && 'cs-sheet--inline') },
      h('div', { className: 'cs-sheet-head' },
        h('div', null, h('h2', { className: 'cs-dialog-title', id: base + '-t' }, p.title), p.description ? h('p', { className: 'cs-dialog-desc' }, p.description) : null),
        h(IconButton, { icon: 'x', label: 'Close', variant: 'neutral', tooltip: false, onClick: p.onClose })),
      h('div', { className: 'cs-sheet-body' }, p.children),
      p.footer ? h('div', { className: 'cs-sheet-foot' }, p.footer) : null);
    return modal ? h('div', { className: 'cs-overlay cs-overlay--sheet' }, panel) : panel;
  }

  function Alert(p) {
    var status = p.status || 'info';
    var role = p.live === 'assertive' ? 'alert' : p.live === 'polite' ? 'status' : undefined;
    return h('div', { className: cx('cs-alert', 'cs-alert--' + status, p.className), role: role },
      h(Icon, { name: p.icon || STATUS_ICON[status], size: 20 }),
      h('div', null,
        h('p', { className: 'cs-alert-title' }, h('span', { className: 'cs-sr' }, ({ success: 'Success: ', warning: 'Warning: ', error: 'Error: ', info: 'Information: ' })[status] || ''), p.title),
        p.children ? h('div', { className: 'cs-alert-body' }, p.children) : null,
        p.actions ? h('div', { className: 'cs-alert-actions' }, p.actions) : null),
      p.onDismiss ? h(IconButton, { icon: 'x', label: 'Dismiss', variant: 'neutral', size: 'small', tooltip: false, onClick: p.onDismiss }) : h('span'));
  }

  function ToastRegion(p) {
    return h('div', { className: cx('cs-toast-region', p.fixed && 'cs-toast-region--fixed'), role: 'status', 'aria-live': 'polite', 'aria-label': 'Notifications' }, p.children);
  }
  function Toast(p) {
    var status = p.status || 'success';
    return h('div', { className: cx('cs-toast', 'cs-toast--' + status) },
      h(Icon, { name: STATUS_ICON[status], size: 20 }),
      h('div', null,
        h('p', { className: 'cs-alert-title' }, h('span', { className: 'cs-sr' }, ({ success: 'Success: ', warning: 'Warning: ', error: 'Error: ', info: 'Information: ' })[status]), p.title),
        p.message ? h('p', { className: 'cs-alert-body' }, p.message) : null,
        p.action ? h('div', { className: 'cs-alert-actions' }, p.action) : null),
      p.onDismiss ? h(IconButton, { icon: 'x', label: 'Dismiss notification', variant: 'neutral', size: 'small', tooltip: false, onClick: p.onDismiss }) : h('span'));
  }

  function Skeleton(p) {
    var variant = p.variant || 'text';
    var lines = p.lines || 1;
    var shapes = [];
    if (variant === 'text') for (var i = 0; i < lines; i++) shapes.push(h('span', { key: i, className: 'cs-skel cs-skel--text', style: { width: i === lines - 1 && lines > 1 ? '60%' : (p.width || '100%') } }));
    else shapes.push(h('span', { key: 0, className: cx('cs-skel', variant === 'circle' && 'cs-skel--circle'), style: { width: p.width || (variant === 'circle' ? 40 : '100%'), height: p.height || (variant === 'circle' ? 40 : 96) } }));
    return h('div', { className: p.className, 'aria-busy': 'true' }, p.label ? h('span', { className: 'cs-sr', role: 'status' }, p.label) : null, h('div', { 'aria-hidden': 'true' }, shapes));
  }

  function EmptyState(p) {
    return h('div', { className: cx('cs-state', p.className) },
      h('span', { className: 'cs-state-icon', 'aria-hidden': 'true' }, h(Icon, { name: p.icon || 'inbox', size: 24 })),
      h(p.headingLevel || 'h2', { className: 'cs-state-title' }, p.title),
      p.description ? h('p', { className: 'cs-state-desc' }, p.description) : null,
      p.action ? h('div', { className: 'cs-row', style: { justifyContent: 'center' } }, p.action) : null);
  }
  function ErrorState(p) {
    return h('div', { className: cx('cs-state', p.className), role: p.live ? 'alert' : undefined },
      h('span', { className: 'cs-state-icon cs-state-icon--error', 'aria-hidden': 'true' }, h(Icon, { name: 'circle-alert', size: 24 })),
      h(p.headingLevel || 'h2', { className: 'cs-state-title' }, p.title || 'We could not load this page'),
      h('p', { className: 'cs-state-desc' }, p.description || 'Your changes are safe. Check your connection and try again.'),
      h('div', { className: 'cs-row', style: { justifyContent: 'center' } }, p.onRetry ? h(Button, { variant: 'secondary', iconStart: 'refresh-cw', onClick: p.onRetry }, p.retryLabel || 'Try again') : null, p.secondary || null),
      p.reference ? h('p', { className: 'cs-state-ref' }, 'Reference: ' + p.reference) : null);
  }
  function PermissionDenied(p) {
    return h('div', { className: cx('cs-state', p.className) },
      h('span', { className: 'cs-state-icon cs-state-icon--neutral', 'aria-hidden': 'true' }, h(Icon, { name: 'lock', size: 24 })),
      h(p.headingLevel || 'h2', { className: 'cs-state-title' }, p.title || 'You do not have access to this area'),
      h('p', { className: 'cs-state-desc' }, p.description || 'Ask your registered manager or an administrator to give your role access.'),
      p.action ? h('div', { className: 'cs-row', style: { justifyContent: 'center' } }, p.action) : null);
  }

  /* Compliance patterns */
  function SignedBanner(p) {
    return h('div', { className: 'cs-banner cs-banner--signed', role: 'note' },
      h(Icon, { name: 'lock', size: 20 }),
      h('p', { className: 'cs-banner-text', style: { margin: 0 } }, h('strong', null, p.title || 'Signed and locked. This record is read-only.'),
        'Signed by ' + p.signedBy + (p.role ? ', ' + p.role : '') + ' on ' + p.signedAt + (p.version ? '. Version ' + p.version + '.' : '.')),
      p.onNewVersion ? h(Button, { variant: 'secondary', size: 'small', iconStart: 'pencil-line', onClick: p.onNewVersion }, p.newVersionLabel || 'Start a new version') : null);
  }

  function ArchivedBanner(p) {
    return h('div', { className: 'cs-banner cs-banner--archived', role: 'note' },
      h(Icon, { name: 'archive', size: 20 }),
      h('p', { className: 'cs-banner-text', style: { margin: 0 } }, h('strong', null, p.title || 'Archived. This record is read-only.'),
        'Archived by ' + p.archivedBy + ' on ' + p.archivedAt + (p.reason ? '. Reason: ' + p.reason : '.')),
      p.onRestore ? h(Button, { variant: 'secondary', size: 'small', iconStart: 'archive-restore', onClick: p.onRestore }, 'Restore') : null);
  }

  var TL_ICON = { created: 'plus', edited: 'pencil-line', signed: 'signature', viewed: 'eye', archived: 'archive', rejected: 'circle-x', uploaded: 'upload', restored: 'archive-restore' };
  function AuditTimeline(p) {
    return h('ol', { className: 'cs-timeline', 'aria-label': p.label || 'Audit history' }, (p.events || []).map(function (ev, i) {
      return h('li', { key: i, className: 'cs-tl-item' },
        h('span', { className: cx('cs-tl-dot', ev.type === 'signed' && 'cs-tl-dot--signed', ev.type === 'rejected' && 'cs-tl-dot--error'), 'aria-hidden': 'true' }, h(Icon, { name: TL_ICON[ev.type] || 'history', size: 16 })),
        h('div', { className: 'cs-tl-main' },
          h('strong', null, ev.actor), ' ', ev.action,
          h('time', { className: 'cs-tl-time', dateTime: ev.iso }, ev.at),
          ev.detail ? h('p', { className: 'cs-tl-detail' }, ev.detail) : null));
    }));
  }

  function VersionCompare(p) {
    function col(side, data) {
      return h('section', { className: 'cs-compare-col', 'aria-label': data.label },
        h('div', { className: 'cs-compare-head' }, h('span', null, data.label), data.badge ? h(StatusBadge, { status: data.badge.status }, data.badge.text) : null),
        h('div', { className: 'cs-compare-body' }, data.blocks.map(function (b, i) {
          if (b.change === 'removed' && side === 'old') return h('div', { key: i, className: 'cs-diff cs-diff--removed' }, h('span', { className: 'cs-diff-tag' }, 'Removed'), h('del', null, b.text));
          if (b.change === 'added' && side === 'new') return h('div', { key: i, className: 'cs-diff cs-diff--added' }, h('span', { className: 'cs-diff-tag' }, 'Added'), h('ins', null, b.text));
          return h('p', { key: i }, b.text);
        })));
    }
    return h('div', { className: 'cs-stack' },
      p.summary ? h('p', { className: 'cs-hint', role: 'status' }, p.summary) : null,
      h('div', { className: 'cs-compare' }, col('old', p.previous), col('new', p.current)));
  }

  function UnsavedChanges(p) {
    useEffect(function () {
      if (!p.guardNavigation) return;
      function warn(e) { e.preventDefault(); e.returnValue = ''; }
      window.addEventListener('beforeunload', warn);
      return function () { window.removeEventListener('beforeunload', warn); };
    }, [p.guardNavigation]);
    return h('div', { className: cx('cs-unsaved', p.sticky && 'cs-unsaved--sticky'), role: 'status', 'aria-live': 'polite' },
      h('span', { className: 'cs-unsaved-text' }, h(Icon, { name: 'triangle-alert', size: 20 }), p.message || 'You have unsaved changes'),
      h('div', { className: 'cs-row' },
        h(Button, { variant: 'ghost', onClick: p.onDiscard }, p.discardLabel || 'Discard changes'),
        h(Button, { variant: 'primary', iconStart: 'save', onClick: p.onSave, loading: p.saving, loadingLabel: 'Saving' }, p.saveLabel || 'Save changes')));
  }

  function BulkConfirm(p) {
    var items = p.items || [];
    var shown = items.slice(0, p.maxListed || 8);
    return h(AlertDialog, {
      open: p.open, inline: p.inline, tone: p.tone || 'danger', title: p.title, onCancel: p.onCancel, onConfirm: p.onConfirm, busy: p.busy, busyLabel: p.busyLabel,
      confirmLabel: p.confirmLabel, description: p.description
    }, h('div', { className: 'cs-stack', style: { gap: 8 } },
      h('p', { className: 'cs-label', style: { margin: 0 } }, p.count + (p.count === 1 ? ' record selected' : ' records selected')),
      h('ul', { className: 'cs-bulk-list' }, shown.map(function (it, i) { return h('li', { key: i }, it); }), items.length > shown.length ? h('li', null, 'and ' + (items.length - shown.length) + ' more') : null)));
  }

  var api = {
    Icon: Icon, Button: Button, IconButton: IconButton, Input: Input, Textarea: Textarea, Select: Select, Checkbox: Checkbox, RadioGroup: RadioGroup, Switch: Switch, DatePicker: DatePicker, FileUpload: FileUpload,
    StatusBadge: StatusBadge, Card: Card, KpiCard: KpiCard, DataTable: DataTable, Tabs: Tabs, Breadcrumbs: Breadcrumbs, SideNav: SideNav, TopBar: TopBar, Dropdown: Dropdown, Tooltip: Tooltip,
    Dialog: Dialog, AlertDialog: AlertDialog, Sheet: Sheet, Alert: Alert, Toast: Toast, ToastRegion: ToastRegion, Skeleton: Skeleton, EmptyState: EmptyState, ErrorState: ErrorState, PermissionDenied: PermissionDenied,
    SignedBanner: SignedBanner, AuditTimeline: AuditTimeline, VersionCompare: VersionCompare, UnsavedChanges: UnsavedChanges, BulkConfirm: BulkConfirm, ArchivedBanner: ArchivedBanner,
    version: '1.1.0'
  };
  window.CareSync = Object.assign(window.CareSync || {}, api);
})();
/* Care Sync Unified 1.1.0: HR provider patterns. Built only from window.CareSync components and canonical tokens. All actions are local simulations. */
(function () {
  'use strict';
  var React = window.React, h = React.createElement;
  var useState = React.useState, useRef = React.useRef, useEffect = React.useEffect, useId = React.useId;
  var C = window.CareSync;

  function cx() { var o = []; for (var i = 0; i < arguments.length; i++) if (arguments[i]) o.push(arguments[i]); return o.join(' '); }
  function useBase() { return 'csp' + useId().replace(/:/g, ''); }
  function focusById(id) { var el = document.getElementById(id); if (el) el.focus(); }
  function nowTime() { var d = new Date(); return ('0' + d.getHours()).slice(-2) + ':' + ('0' + d.getMinutes()).slice(-2); }
  function Live(p) { return h('p', { className: p.visible ? 'cs-pat-live' : 'cs-sr', role: 'status', 'aria-live': 'polite' }, p.children || ''); }
  function Label(p) { return h('span', { className: 'cs-pat-label' }, p.children); }
  function Facts(p) {
    return h('dl', { className: 'cs-pat-facts' }, (p.items || []).map(function (f, i) {
      return h('div', { key: i, className: 'cs-pat-fact' }, h('dt', null, f.label), h('dd', null, f.value));
    }));
  }

  var OWNERSHIP = { linked: { text: 'Linked record', icon: 'link' }, held: { text: 'Held here', icon: 'archive' } };
  var VERIFICATION = { verified: { text: 'Verified', status: 'success' }, unverified: { text: 'Not verified', status: 'warning' }, rejected: { text: 'Rejected', status: 'error' }, 'not-required': { text: 'Not required', status: 'neutral' } };
  var EXPIRY = { valid: { text: 'In date', status: 'success' }, expiring: { text: 'Expiring soon', status: 'warning' }, expired: { text: 'Expired', status: 'error' }, none: { text: 'No expiry', status: 'neutral', icon: 'minus' } };
  var VISIBILITY = { staff: { text: 'Staff and managers', icon: 'eye' }, managers: { text: 'Managers only', icon: 'eye-off' }, restricted: { text: 'Restricted', icon: 'lock' } };

  function Ownership(p) { var o = OWNERSHIP[p.value] || OWNERSHIP.held; return h(C.StatusBadge, { status: 'neutral', icon: o.icon }, o.text); }
  function Verification(p) { var v = VERIFICATION[p.value] || VERIFICATION.unverified; return h(C.StatusBadge, { status: v.status }, v.text); }
  function Expiry(p) {
    var e = p.expiry || { status: 'none' }; var s = EXPIRY[e.status] || EXPIRY.none;
    return h('span', { className: 'cs-pat-expiry' }, h(C.StatusBadge, { status: s.status, icon: s.icon }, s.text), e.date ? h('span', { className: 'cs-pat-sub' }, (e.status === 'expired' ? 'Expired ' : 'Until ') + e.date) : null);
  }
  function Visibility(p) { var v = VISIBILITY[p.value] || VISIBILITY.staff; return h('span', { className: 'cs-pat-vis' }, h(C.Icon, { name: v.icon, size: 16 }), v.text); }

  /* 1. Record preview ------------------------------------------------------ */
  function PatternRecordPreview(p) {
    var state = p.state || 'ready';
    var r = p.record || {};
    var evidence = state === 'no-evidence' ? [] : (r.evidence || []);
    var title = state === 'restricted' ? 'Restricted record' : state === 'error' ? 'Record preview' : (r.title || 'Record preview');
    var body;
    if (state === 'loading') {
      body = h('div', { className: 'cs-pat-stack' },
        h(C.Skeleton, { variant: 'text', lines: 2, label: 'Loading record preview' }),
        h(C.Skeleton, { variant: 'block', height: 88 }),
        h(C.Skeleton, { variant: 'text', lines: 4 }));
    } else if (state === 'restricted') {
      body = h(C.PermissionDenied, { headingLevel: 'h3', title: 'You cannot view this record', description: p.restrictedMessage || 'This record is limited to managers. Ask a registered manager or an administrator if you need access.' });
    } else if (state === 'error') {
      body = h(C.ErrorState, { headingLevel: 'h3', live: true, title: 'We could not load this record', description: 'Nothing has changed. Check your connection and try again.', onRetry: p.onRetry, reference: 'SAMPLE-ERR-0001' });
    } else {
      var tabs = [
        { id: 'overview', label: 'Overview', content: h(Facts, { items: r.facts }) },
        { id: 'evidence', label: 'Evidence', count: evidence.length, content: evidence.length
          ? h('ul', { className: 'cs-pat-evlist' }, evidence.map(function (e, i) {
              return h('li', { key: i, className: 'cs-pat-evitem' },
                h('div', null, h('p', { className: 'cs-pat-strong' }, e.name), h('p', { className: 'cs-pat-sub' }, e.id)),
                h('div', { className: 'cs-row' }, h(Ownership, { value: e.ownership }), h(Verification, { value: e.verification })));
            }))
          : h(C.EmptyState, { headingLevel: 'h3', icon: 'file-text', title: 'No evidence attached', description: 'No evidence is attached to this record yet. That alone does not make the record invalid; check the owning source record.' }) },
        { id: 'history', label: 'History', content: h(C.AuditTimeline, { events: r.history || [], label: 'Record history' }) }
      ];
      body = h('div', { className: 'cs-pat-stack' },
        h('div', { className: 'cs-pat-person' },
          h('span', { className: 'cs-avatar', 'aria-hidden': 'true' }, r.initials || ''),
          h('div', null, h('p', { className: 'cs-pat-strong' }, r.person), h('p', { className: 'cs-pat-sub' }, r.role)),
          h('p', { className: 'cs-pat-status' }, h(Label, null, 'Status'), r.status ? h(C.StatusBadge, { status: r.status.tone }, r.status.text) : null)),
        r.nextAction ? h('section', { className: 'cs-pat-next', 'aria-label': 'Next action' },
          h('div', null, h(Label, null, 'Next action'), h('p', { className: 'cs-pat-strong' }, r.nextAction.text), r.nextAction.due ? h('p', { className: 'cs-pat-sub' }, 'Due ' + r.nextAction.due) : null),
          r.nextAction.label ? h(C.Button, { variant: 'secondary', onClick: p.onNextAction }, r.nextAction.label) : null) : null,
        h(C.Tabs, { key: state + (p.defaultTab || ''), label: 'Record details', tabs: tabs, defaultTab: p.defaultTab || 'overview' }));
    }
    var canOpenSource = state !== 'restricted' && state !== 'error' && state !== 'loading' && r.source;
    /* Docked (inline) mode is controlled too: open === false hides it, and X, Close and Escape all call onClose. */
    if (p.inline && p.open === false) return null;
    var sheet = h(C.Sheet, {
      open: p.open, inline: p.inline, onClose: p.onClose, title: title,
      description: p.context || r.context,
      footer: [
        h(C.Button, { key: 'close', variant: 'secondary', onClick: p.onClose }, 'Close'),
        canOpenSource ? h('a', { key: 'src', className: 'cs-btn cs-btn--primary', href: r.source.href || '#' }, h(C.Icon, { name: 'external-link', size: 20 }), h('span', null, 'Open source record'), h('span', { className: 'cs-sr' }, ', ' + r.source.label)) : null
      ]
    }, body);
    if (!p.inline) return sheet;
    return h('div', { className: 'cs-pat-docked', onKeyDown: function (e) { if (e.key === 'Escape' && p.onClose) { e.stopPropagation(); p.onClose(); } } }, sheet);
  }

  /* 2. Evidence register --------------------------------------------------- */
  var NO_FILTERS = { ownership: '', verification: '', expiry: '' };
  function PatternEvidenceRegister(p) {
    var base = useBase();
    var s1 = useState(''); var q = s1[0], setQ = s1[1];
    var s2 = useState(NO_FILTERS); var f = s2[0], setF = s2[1];
    var s3 = useState(p.items || []); var items = s3[0], setItems = s3[1];
    var s4 = useState(null); var reviewing = s4[0], setReviewing = s4[1];
    var s5 = useState(''); var decision = s5[0], setDecision = s5[1];
    var s6 = useState(''); var live = s6[0], setLive = s6[1];
    var s7 = useState(''); var decisionError = s7[0], setDecisionError = s7[1];
    useEffect(function () { setItems(p.items || []); }, [p.items]);
    var state = p.state || 'ready';
    var active = q !== '' || f.ownership || f.verification || f.expiry;
    var shown = items.filter(function (it) {
      var needle = q.trim().toLowerCase();
      if (needle && (it.name + ' ' + it.person + ' ' + it.id + ' ' + (it.type || '')).toLowerCase().indexOf(needle) < 0) return false;
      if (f.ownership && it.ownership !== f.ownership) return false;
      if (f.verification && it.verification !== f.verification) return false;
      if (f.expiry && (it.expiry || {}).status !== f.expiry) return false;
      return true;
    });
    function reset() { setQ(''); setF(NO_FILTERS); setLive('Filters reset. Showing all ' + items.length + ' documents.'); focusById(base + '-q'); }
    function setFilter(k) { return function (e) { var n = Object.assign({}, f); n[k] = e.target.value; setF(n); }; }
    function openReview(it) { setReviewing(it); setDecision(''); setDecisionError(''); }
    function saveReview() {
      if (!decision) { setDecisionError('Choose a verification outcome.'); focusById(base + '-dec-0'); return; }
      setItems(items.map(function (it) { return it.id === reviewing.id ? Object.assign({}, it, { verification: decision }) : it; }));
      setLive(reviewing.name + ' for ' + reviewing.person + ' marked as ' + VERIFICATION[decision].text.toLowerCase() + '. Local simulation, nothing was sent.');
      if (p.onReview) p.onReview(reviewing, decision);
      setReviewing(null);
    }
    function actions(it) {
      return h('div', { className: 'cs-pat-actions' },
        h(C.Button, { variant: 'secondary', onClick: function () { openReview(it); }, 'aria-label': 'Review ' + it.name + ' for ' + it.person }, 'Review'),
        h('a', { className: 'cs-btn cs-btn--ghost', href: (it.source && it.source.href) || '#', 'aria-label': (it.ownership === 'linked' ? 'Open linked source record ' : 'Open document ') + (it.source ? it.source.label : it.id) },
          h(C.Icon, { name: it.ownership === 'linked' ? 'external-link' : 'file-text', size: 20 }), h('span', null, it.ownership === 'linked' ? 'Source record' : 'Open document')));
    }
    var content;
    if (state === 'loading') content = h('div', { className: 'cs-pat-stack', style: { padding: 16 } }, h(C.Skeleton, { lines: 1, label: 'Loading evidence register' }), [0, 1, 2, 3].map(function (i) { return h(C.Skeleton, { key: i, variant: 'block', height: 56 }); }));
    else if (state === 'error') content = h(C.ErrorState, { headingLevel: 'h3', live: true, title: 'We could not load the evidence register', description: 'Documents are not affected. Try again, or come back later.', onRetry: p.onRetry, reference: 'SAMPLE-ERR-0002' });
    else if (!items.length) content = h(C.EmptyState, { headingLevel: 'h3', icon: 'inbox', title: 'No documents yet', description: 'Documents held here or linked from other records will appear here.' });
    else if (!shown.length) content = h(C.EmptyState, { headingLevel: 'h3', icon: 'search', title: 'No documents match your search', description: 'Try different words, or reset the filters to see all ' + items.length + ' documents.', action: h(C.Button, { variant: 'secondary', iconStart: 'rotate-ccw', onClick: reset }, 'Reset filters') });
    else content = h('div', null,
      h('div', { className: 'cs-pat-wide cs-scroll', role: 'region', 'aria-labelledby': base + '-cap', tabIndex: 0 },
        h('table', { className: 'cs-table cs-pat-table' },
          h('caption', { className: 'cs-sr', id: base + '-cap' }, (p.title || 'Evidence register') + ', ' + shown.length + ' documents'),
          h('thead', null, h('tr', null, ['Document', 'Person', 'Ownership', 'Verification', 'Expiry', 'Visibility', 'Actions'].map(function (t) { return h('th', { key: t, scope: 'col' }, t); }))),
          h('tbody', null, shown.map(function (it) {
            return h('tr', { key: it.id },
              h('th', { scope: 'row', className: 'cs-pat-docname' }, h('span', { className: 'cs-pat-strong' }, it.name), h('span', { className: 'cs-pat-sub' }, (it.type ? it.type + ', ' : '') + it.id)),
              h('td', null, it.person),
              h('td', null, h(Ownership, { value: it.ownership }), it.ownership === 'linked' && it.source ? h('span', { className: 'cs-pat-sub' }, it.source.label) : null),
              h('td', null, h(Verification, { value: it.verification })),
              h('td', null, h(Expiry, { expiry: it.expiry })),
              h('td', null, h(Visibility, { value: it.visibility })),
              h('td', null, actions(it)));
          })))),
      h('ul', { className: 'cs-pat-cards', 'aria-label': (p.title || 'Evidence register') + ', ' + shown.length + ' documents' }, shown.map(function (it) {
        return h('li', { key: it.id, className: 'cs-pat-card' },
          h('h3', { className: 'cs-pat-cardtitle' }, it.name), h('p', { className: 'cs-pat-sub' }, it.person + ', ' + it.id),
          h('dl', { className: 'cs-pat-facts' },
            h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Ownership'), h('dd', null, h(Ownership, { value: it.ownership }), it.ownership === 'linked' && it.source ? h('span', { className: 'cs-pat-sub' }, it.source.label) : null)),
            h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Verification'), h('dd', null, h(Verification, { value: it.verification }))),
            h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Expiry'), h('dd', null, h(Expiry, { expiry: it.expiry }))),
            h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Visibility'), h('dd', null, h(Visibility, { value: it.visibility })))),
          actions(it));
      })));
    return h('section', { className: 'cs-pat cs-pat-register', 'aria-labelledby': base + '-title' },
      h('div', { className: 'cs-pat-head' },
        h('h2', { className: 'cs-card-title', id: base + '-title' }, p.title || 'Evidence register'),
        h('p', { className: 'cs-card-desc' }, 'Ownership, verification, expiry and visibility are separate facts. A document being listed here does not mean it is verified or valid.')),
      state === 'ready' && items.length ? h('div', { className: 'cs-pat-toolbar', role: 'search', 'aria-label': 'Filter documents' },
        h(C.Input, { id: base + '-q', label: 'Search documents', type: 'search', value: q, onChange: function (e) { setQ(e.target.value); }, hint: 'Name, person or ID' }),
        h(C.Select, { id: base + '-own', label: 'Ownership', value: f.ownership, onChange: setFilter('ownership'), options: [{ value: '', label: 'All ownership' }, { value: 'linked', label: 'Linked record' }, { value: 'held', label: 'Held here' }] }),
        h(C.Select, { id: base + '-ver', label: 'Verification', value: f.verification, onChange: setFilter('verification'), options: [{ value: '', label: 'All verification' }, { value: 'verified', label: 'Verified' }, { value: 'unverified', label: 'Not verified' }, { value: 'rejected', label: 'Rejected' }, { value: 'not-required', label: 'Not required' }] }),
        h(C.Select, { id: base + '-exp', label: 'Expiry', value: f.expiry, onChange: setFilter('expiry'), options: [{ value: '', label: 'All expiry' }, { value: 'valid', label: 'In date' }, { value: 'expiring', label: 'Expiring soon' }, { value: 'expired', label: 'Expired' }, { value: 'none', label: 'No expiry' }] }),
        h('div', { className: 'cs-pat-reset' }, h(C.Button, { variant: 'secondary', iconStart: 'rotate-ccw', onClick: reset, disabled: !active }, 'Reset filters'))) : null,
      state === 'ready' && items.length ? h('p', { className: 'cs-pat-count', role: 'status', 'aria-live': 'polite' }, 'Showing ' + shown.length + ' of ' + items.length + ' documents' + (active ? ' (filtered)' : '')) : null,
      content,
      h(Live, { visible: !!live }, live),
      h(C.Dialog, {
        open: !!reviewing, onClose: function () { setReviewing(null); }, title: reviewing ? 'Review ' + reviewing.name : 'Review',
        description: reviewing ? reviewing.person + ', ' + reviewing.id + '. Recording an outcome here is a local simulation.' : '',
        footer: [h(C.Button, { key: 'c', variant: 'secondary', onClick: function () { setReviewing(null); } }, 'Cancel'), h(C.Button, { key: 's', onClick: saveReview }, 'Save review')]
      }, reviewing ? h(C.RadioGroup, { id: base + '-dec', legend: 'Verification outcome', required: true, error: decisionError, onChange: function (e) { setDecision(e.target.value); setDecisionError(''); },
        hint: 'Verification is separate from expiry. A verified document can still be expired.',
        options: [{ value: 'verified', label: 'Verified', hint: 'You have checked the original or a trusted source' }, { value: 'unverified', label: 'Not verified yet' }, { value: 'rejected', label: 'Rejected', hint: 'The document cannot be accepted' }] }) : null));
  }

  /* 3. Guided wizard ------------------------------------------------------- */
  var STEPS = ['Choose item', 'Details', 'Review'];
  var EMPTY = { item: '', recipient: '', date: '', condition: '', notes: '' };
  function PatternGuidedWizard(p) {
    var base = useBase();
    var items = p.items || [], people = p.people || [];
    var s1 = useState(0); var step = s1[0], setStep = s1[1];
    var s2 = useState([false, false, false]); var done = s2[0], setDone = s2[1];
    var s3 = useState(EMPTY); var data = s3[0], setData = s3[1];
    var s4 = useState({}); var errors = s4[0], setErrors = s4[1];
    var s5 = useState(false); var confirmDiscard = s5[0], setConfirmDiscard = s5[1];
    var s6 = useState(null); var receipt = s6[0], setReceipt = s6[1];
    var s7 = useState(false); var busy = s7[0], setBusy = s7[1];
    var s8 = useState(''); var live = s8[0], setLive = s8[1];
    var s9 = useState(0); var errTick = s9[0], setErrTick = s9[1];
    var s10 = useState(0); var resetKey = s10[0], setResetKey = s10[1];
    var summaryRef = useRef(null), headRef = useRef(null), receiptRef = useRef(null), first = useRef(true);
    var dirty = Object.keys(data).some(function (k) { return data[k] !== ''; });
    useEffect(function () { if (errTick && summaryRef.current) summaryRef.current.focus(); }, [errTick]);
    useEffect(function () { if (first.current) { first.current = false; return; } if (!receipt && headRef.current) headRef.current.focus(); }, [step]);
    useEffect(function () { if (receipt && receiptRef.current) receiptRef.current.focus(); }, [receipt]);
    function set(k) { return function (e) { var n = Object.assign({}, data); n[k] = e.target.value; setData(n); }; }
    function itemLabel(v) { var m = items.filter(function (i) { return i.value === v; })[0]; return m ? m.label : v; }
    function validate(i) {
      var e = [];
      if (i === 0 && !data.item) e.push({ field: 'item', target: base + '-item-0', text: 'Choose the item you are handing over.' });
      if (i === 1) {
        if (!data.recipient) e.push({ field: 'recipient', target: base + '-recipient', text: 'Choose who is receiving the item.' });
        if (!data.date) e.push({ field: 'date', target: base + '-date', text: 'Enter the handover date.' });
        else if (data.date > new Date().toISOString().slice(0, 10)) e.push({ field: 'date', target: base + '-date', text: 'The handover date must be today or in the past.' });
        if (!data.condition) e.push({ field: 'condition', target: base + '-condition', text: 'Choose the condition of the item.' });
      }
      return e;
    }
    function errFor(k) { var m = (errors.list || []).filter(function (x) { return x.field === k; })[0]; return m ? m.text : undefined; }
    function next() {
      var e = validate(step);
      if (e.length) { setErrors({ list: e }); setErrTick(errTick + 1); return; }
      setErrors({}); var d = done.slice(); d[step] = true; setDone(d); setStep(step + 1);
    }
    function back() { setErrors({}); setStep(step - 1); }
    function jump(i) { if (done[i] && i !== step) { setErrors({}); setStep(i); } }
    function reset(msg) { setResetKey(resetKey + 1); setData(EMPTY); setDone([false, false, false]); setErrors({}); setStep(0); setReceipt(null); setLive(msg); }
    function cancel() { if (dirty) setConfirmDiscard(true); else { reset('Nothing to discard.'); if (p.onDiscard) p.onDiscard(); } }
    function submit() {
      setBusy(true); setLive('Recording handover.');
      setTimeout(function () {
        setBusy(false);
        var rec = { ref: 'HO-SAMPLE-' + String(1 + Math.floor(Math.random() * 9000)).padStart(4, '0'), item: itemLabel(data.item), recipient: data.recipient, date: data.date, condition: data.condition, notes: data.notes, at: nowTime() };
        setReceipt(rec); setLive('Handover recorded locally. Reference ' + rec.ref + '.');
        if (p.onSubmit) p.onSubmit(rec);
      }, p.delay == null ? 600 : p.delay);
    }
    var stepper = h('nav', { className: 'cs-pat-steps', 'aria-label': 'Progress' }, h('ol', null, STEPS.map(function (label, i) {
      var st = receipt ? 'completed' : i === step ? 'current' : done[i] ? 'completed' : 'future';
      var text = st === 'completed' ? 'Completed' : st === 'current' ? 'Current step' : 'Not started';
      var inner = [h('span', { key: 'm', className: 'cs-pat-stepmark', 'aria-hidden': 'true' }, st === 'completed' ? h(C.Icon, { name: 'check', size: 16 }) : String(i + 1)),
        h('span', { key: 't', className: 'cs-pat-steptext' }, h('span', { className: 'cs-pat-steplabel' }, label), h('span', { className: 'cs-pat-stepstate' }, text))];
      var canJump = st === 'completed' && !receipt;
      return h('li', { key: label, className: 'cs-pat-step cs-pat-step--' + st },
        canJump ? h('button', { type: 'button', className: 'cs-pat-stepbtn', onClick: function () { jump(i); }, 'aria-label': 'Step ' + (i + 1) + ', ' + label + ', completed. Return to this step' }, inner)
          : h('span', { className: 'cs-pat-stepbtn', 'aria-current': st === 'current' ? 'step' : undefined }, h('span', { className: 'cs-sr' }, 'Step ' + (i + 1) + ', '), inner));
    })));
    var summary = errors.list && errors.list.length ? h('div', { ref: summaryRef, tabIndex: -1, className: 'cs-pat-errsum', 'aria-labelledby': base + '-errh' },
      h('h3', { id: base + '-errh', className: 'cs-alert-title' }, h(C.Icon, { name: 'circle-alert', size: 20 }), ' There is a problem'),
      h('ul', null, errors.list.map(function (e, i) { return h('li', { key: i }, h('a', { href: '#' + e.target, onClick: function (ev) { ev.preventDefault(); focusById(e.target); } }, e.text)); }))) : null;
    var panel;
    if (receipt) {
      panel = h('div', { className: 'cs-pat-stack' },
        h('h3', { ref: receiptRef, tabIndex: -1, className: 'cs-pat-h' }, 'Handover recorded'),
        h(C.Alert, { status: 'success', title: 'Reference ' + receipt.ref }, 'Recorded locally in this preview at ' + receipt.at + '. No signature was captured and nothing was sent anywhere.'),
        h(Facts, { items: [{ label: 'Item', value: receipt.item }, { label: 'Recipient', value: receipt.recipient }, { label: 'Handover date', value: receipt.date }, { label: 'Condition', value: receipt.condition }, { label: 'Notes', value: receipt.notes || 'None' }] }),
        h('div', { className: 'cs-row' }, h(C.Button, { variant: 'secondary', iconStart: 'plus', onClick: function () { reset('Started a new handover.'); } }, 'Start another handover')));
    } else if (step === 0) {
      panel = h(C.RadioGroup, { key: 'item', id: base + '-item', name: base + '-item', legend: 'Which item are you handing over?', required: true, defaultValue: data.item, error: errFor('item'), onChange: set('item'), options: items });
    } else if (step === 1) {
      panel = h('div', { className: 'cs-pat-grid2' },
        h(C.Select, { id: base + '-recipient', label: 'Recipient', required: true, value: data.recipient, onChange: set('recipient'), error: errFor('recipient'), placeholder: 'Choose a person', options: people }),
        h(C.DatePicker, { id: base + '-date', label: 'Handover date', required: true, value: data.date, onChange: set('date'), error: errFor('date') }),
        h(C.Select, { id: base + '-condition', label: 'Condition', required: true, value: data.condition, onChange: set('condition'), error: errFor('condition'), placeholder: 'Choose a condition', options: ['New', 'Good', 'Fair, with visible wear', 'Needs repair'] }),
        h(C.Textarea, { id: base + '-notes', className: 'cs-pat-span', label: 'Notes', optional: true, defaultValue: data.notes, onChange: set('notes'), maxLength: 300, hint: 'For example, accessories included.' }));
    } else {
      var rows = [{ label: 'Item', value: itemLabel(data.item), step: 0 }, { label: 'Recipient', value: data.recipient, step: 1 }, { label: 'Handover date', value: data.date, step: 1 }, { label: 'Condition', value: data.condition, step: 1 }, { label: 'Notes', value: data.notes || 'None', step: 1 }];
      panel = h('div', { className: 'cs-pat-stack' },
        h('dl', { className: 'cs-pat-review' }, rows.map(function (r) {
          return h('div', { key: r.label, className: 'cs-pat-reviewrow' }, h('dt', null, r.label), h('dd', null, r.value),
            h('dd', null, h(C.Button, { variant: 'ghost', onClick: function () { jump(r.step); }, 'aria-label': 'Change ' + r.label.toLowerCase() }, 'Change')));
        })),
        h(C.Alert, { status: 'info', title: 'Check before you record it' }, 'This preview records the handover locally only. It does not capture a signature or send anything.'));
    }
    return h('section', { className: 'cs-pat cs-pat-wizard', 'aria-labelledby': base + '-title' },
      h('div', { className: 'cs-pat-head' }, h('h2', { className: 'cs-card-title', id: base + '-title' }, p.title || 'Equipment handover'), h('p', { className: 'cs-card-desc' }, 'Synthetic local example. Three steps: choose the item, add details, then review.')),
      stepper,
      h('div', { className: 'cs-pat-body', key: 'body-' + resetKey },
        receipt ? null : h('h3', { ref: headRef, tabIndex: -1, className: 'cs-pat-h' }, 'Step ' + (step + 1) + ' of 3: ' + STEPS[step]),
        summary, panel),
      receipt ? null : h('div', { className: 'cs-pat-foot' },
        h(C.Button, { variant: 'ghost', onClick: cancel }, 'Cancel'),
        h('div', { className: 'cs-row' },
          step > 0 ? h(C.Button, { variant: 'secondary', iconStart: 'chevron-left', onClick: back }, 'Back') : null,
          step < 2 ? h(C.Button, { iconEnd: 'chevron-right', onClick: next }, 'Continue') : h(C.Button, { iconStart: 'check', onClick: submit, loading: busy, loadingLabel: 'Recording' }, 'Record handover'))),
      h(Live, null, live),
      h(C.AlertDialog, { open: confirmDiscard, title: 'Discard this handover?', description: 'The details you entered will be removed. You cannot undo this.', confirmLabel: 'Discard handover', cancelLabel: 'Keep editing',
        onCancel: function () { setConfirmDiscard(false); }, onConfirm: function () { setConfirmDiscard(false); reset('Handover discarded.'); if (p.onDiscard) p.onDiscard(); } }));
  }

  /* 4. Decision queue ------------------------------------------------------ */
  function PatternDecisionQueue(p) {
    var base = useBase();
    var pageSize = p.pageSize || 4;
    var s1 = useState(p.requests || []); var rows = s1[0], setRows = s1[1];
    var s2 = useState(0); var page = s2[0], setPage = s2[1];
    var s3 = useState([]); var sel = s3[0], setSel = s3[1];
    var s4 = useState(null); var dialog = s4[0], setDialog = s4[1];
    var s5 = useState(''); var reason = s5[0], setReason = s5[1];
    var s6 = useState(''); var reasonError = s6[0], setReasonError = s6[1];
    var s7 = useState([]); var processing = s7[0], setProcessing = s7[1];
    var s8 = useState(null); var result = s8[0], setResult = s8[1];
    var s9 = useState([]); var receipts = s9[0], setReceipts = s9[1];
    var s10 = useState({}); var failed = s10[0], setFailed = s10[1];
    var s11 = useState(''); var live = s11[0], setLive = s11[1];
    var attempts = useRef({}), seq = useRef(0);
    var failIds = p.failIds || [];
    var pages = Math.max(1, Math.ceil(rows.length / pageSize));
    var pg = Math.min(page, pages - 1);
    var view = rows.slice(pg * pageSize, pg * pageSize + pageSize);
    var viewIds = view.map(function (r) { return r.id; });
    var selOnPage = sel.filter(function (id) { return viewIds.indexOf(id) >= 0; });
    var allOn = viewIds.length > 0 && selOnPage.length === viewIds.length;
    var busy = processing.length > 0;
    function toggle(id) { setSel(sel.indexOf(id) >= 0 ? sel.filter(function (x) { return x !== id; }) : sel.concat([id])); }
    function toggleAll() { setSel(allOn ? [] : viewIds.slice()); }
    function goPage(n) { var had = selOnPage.length; setPage(n); setSel([]); setLive('Page ' + (n + 1) + ' of ' + pages + '.' + (had ? ' Selection cleared; decisions apply to one page at a time.' : '')); }
    function byId(id) { return rows.filter(function (r) { return r.id === id; })[0]; }
    function openDialog(kind) { setReason(''); setReasonError(''); setDialog(kind); }
    function apply(kind, ids, why) {
      setDialog(null); setResult(null); setProcessing(ids);
      setLive('Applying ' + (kind === 'approve' ? 'approval' : 'decline') + ' to ' + ids.length + (ids.length === 1 ? ' request.' : ' requests.'));
      setTimeout(function () {
        var ok = [], bad = [];
        ids.forEach(function (id) {
          var n = (attempts.current[id] || 0) + 1; attempts.current[id] = n;
          if (failIds.indexOf(id) >= 0 && n === 1) bad.push(id); else ok.push(id);
        });
        var t = nowTime();
        var newReceipts = ok.map(function (id) { var r = byId(id); seq.current += 1; return { ref: 'AUD-SAMPLE-' + String(seq.current).padStart(4, '0'), action: kind === 'approve' ? 'Approved' : 'Declined', id: id, person: r ? r.person : '', at: t, reason: why }; });
        setReceipts(function (cur) { return cur.concat(newReceipts); });
        setRows(function (cur) { return cur.filter(function (r) { return ok.indexOf(r.id) < 0; }); });
        setFailed(function (cur) { var f = Object.assign({}, cur); ok.forEach(function (id) { delete f[id]; }); bad.forEach(function (id) { f[id] = true; }); return f; });
        setSel(bad.slice()); setProcessing([]);
        var verb = kind === 'approve' ? 'approved' : 'declined';
        setResult({ kind: kind, ok: ok, bad: bad, reason: why });
        setLive(bad.length ? ok.length + ' ' + verb + ' and cleared. ' + bad.length + ' could not be saved and ' + (bad.length === 1 ? 'is' : 'are') + ' still selected.' : ok.length + ' ' + verb + ' and cleared from the queue.');
      }, p.delay == null ? 900 : p.delay);
    }
    function confirm() {
      if (dialog === 'decline' && !reason.trim()) { setReasonError('Enter a reason for declining. It is shared with each person.'); focusById(base + '-reason'); return; }
      apply(dialog, selOnPage, dialog === 'decline' ? reason.trim() : '');
    }
    function statusOf(r) {
      if (processing.indexOf(r.id) >= 0) return h(C.StatusBadge, { status: 'info', icon: 'clock' }, 'Processing');
      if (failed[r.id]) return h(C.StatusBadge, { status: 'error' }, 'Failed, not saved');
      return h(C.StatusBadge, { status: 'neutral', icon: 'clock' }, 'Pending');
    }
    function warnings(r) { return r.warnings && r.warnings.length ? h('ul', { className: 'cs-pat-warn' }, r.warnings.map(function (w, i) { return h('li', { key: i }, h(C.StatusBadge, { status: 'warning' }, w)); })) : h('span', { className: 'cs-pat-sub' }, 'None'); }
    function rowCheck(r) { return h(C.Checkbox, { label: 'Select request ' + r.id + ' from ' + r.person, hideLabel: true, checked: sel.indexOf(r.id) >= 0, disabled: busy, onChange: function () { toggle(r.id); } }); }
    var selected = selOnPage.map(byId).filter(Boolean);
    return h('section', { className: 'cs-pat cs-pat-queue', 'aria-labelledby': base + '-title', 'aria-busy': busy ? 'true' : undefined },
      h('div', { className: 'cs-pat-head' }, h('h2', { className: 'cs-card-title', id: base + '-title' }, p.title || 'Decision queue'), h('p', { className: 'cs-card-desc' }, 'Synthetic requests. Decisions are simulated locally and apply only to the requests selected on this page.')),
      result ? h(C.Alert, {
        status: result.bad.length ? 'warning' : 'success', live: 'polite',
        title: result.bad.length ? result.bad.length + ' of ' + (result.ok.length + result.bad.length) + ' requests could not be saved' : result.ok.length + (result.ok.length === 1 ? ' request ' : ' requests ') + (result.kind === 'approve' ? 'approved' : 'declined'),
        actions: result.bad.length ? h(C.Button, { variant: 'secondary', iconStart: 'rotate-ccw', onClick: function () { apply(result.kind, result.bad, result.reason); } }, 'Retry failed (' + result.bad.length + ')') : null,
        onDismiss: function () { setResult(null); }
      }, result.bad.length ? result.ok.length + ' ' + (result.kind === 'approve' ? 'approved' : 'declined') + ' and cleared from the queue. The failed ' + (result.bad.length === 1 ? 'request is' : 'requests are') + ' still selected. Retry failed tries only ' + (result.bad.length === 1 ? 'that request' : 'those requests') + '.' : 'They have been cleared from the queue. See the audit receipt below.') : null,
      rows.length ? h('div', { className: 'cs-pat-selbar' },
        h('div', { className: 'cs-pat-selall' }, h(C.Checkbox, { label: 'Select all ' + view.length + ' on this page', checked: allOn, indeterminate: !allOn && selOnPage.length > 0, disabled: busy, onChange: toggleAll })),
        h('p', { className: 'cs-pat-selcount', role: 'status', 'aria-live': 'polite' }, h('strong', null, selOnPage.length + ' of ' + view.length), ' on page ' + (pg + 1) + ' selected. Requests on other pages are not selected.'),
        h('div', { className: 'cs-pat-actions' },
          h(C.Button, { iconStart: 'check', disabled: !selOnPage.length || busy, onClick: function () { openDialog('approve'); } }, 'Approve selected'),
          h(C.Button, { variant: 'secondary', iconStart: 'x', disabled: !selOnPage.length || busy, onClick: function () { openDialog('decline'); } }, 'Decline selected'))) : null,
      rows.length ? h('div', null,
        h('div', { className: 'cs-pat-wide cs-scroll', role: 'region', 'aria-labelledby': base + '-cap', tabIndex: 0 },
          h('table', { className: 'cs-table cs-pat-table' },
            h('caption', { className: 'cs-sr', id: base + '-cap' }, 'Requests awaiting a decision, page ' + (pg + 1) + ' of ' + pages),
            h('thead', null, h('tr', null, h('th', { scope: 'col' }, h('span', { className: 'cs-sr' }, 'Select')), ['Person', 'Request', 'Reason', 'Age', 'Warnings', 'Status'].map(function (t) { return h('th', { key: t, scope: 'col' }, t); }))),
            h('tbody', null, view.map(function (r) {
              return h('tr', { key: r.id, 'aria-selected': sel.indexOf(r.id) >= 0 ? 'true' : 'false' },
                h('td', { className: 'cs-pat-checkcell' }, rowCheck(r)),
                h('th', { scope: 'row' }, h('span', { className: 'cs-pat-strong' }, r.person), h('span', { className: 'cs-pat-sub' }, r.role)),
                h('td', null, h('span', { className: 'cs-pat-strong' }, r.request), h('span', { className: 'cs-pat-sub' }, r.id)),
                h('td', null, r.reason), h('td', null, r.age), h('td', null, warnings(r)), h('td', null, statusOf(r)));
            })))),
        h('ul', { className: 'cs-pat-cards', 'aria-label': 'Requests awaiting a decision, page ' + (pg + 1) + ' of ' + pages }, view.map(function (r) {
          return h('li', { key: r.id, className: 'cs-pat-card' + (sel.indexOf(r.id) >= 0 ? ' cs-pat-card--selected' : '') },
            h('div', { className: 'cs-pat-cardhead' }, rowCheck(r), h('div', null, h('h3', { className: 'cs-pat-cardtitle' }, r.person), h('p', { className: 'cs-pat-sub' }, r.role + ', ' + r.id))),
            h('dl', { className: 'cs-pat-facts' },
              h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Request'), h('dd', null, r.request)),
              h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Reason'), h('dd', null, r.reason)),
              h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Age'), h('dd', null, r.age)),
              h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Warnings'), h('dd', null, warnings(r))),
              h('div', { className: 'cs-pat-fact' }, h('dt', null, 'Status'), h('dd', null, statusOf(r)))));
        })),
        h('div', { className: 'cs-table-foot' },
          h('span', null, 'Page ' + (pg + 1) + ' of ' + pages + ', ' + rows.length + (rows.length === 1 ? ' request' : ' requests') + ' waiting'),
          h('nav', { className: 'cs-row', 'aria-label': 'Queue pages' },
            h(C.Button, { variant: 'secondary', iconStart: 'chevron-left', disabled: pg === 0 || busy, onClick: function () { goPage(pg - 1); } }, 'Previous'),
            h(C.Button, { variant: 'secondary', iconEnd: 'chevron-right', disabled: pg >= pages - 1 || busy, onClick: function () { goPage(pg + 1); } }, 'Next'))))
        : h(C.EmptyState, { headingLevel: 'h3', icon: 'list-checks', title: 'No requests waiting', description: 'Every request in this queue has a decision.' }),
      receipts.length ? h('section', { className: 'cs-pat-receipt', 'aria-labelledby': base + '-rec' },
        h('h3', { id: base + '-rec', className: 'cs-pat-h' }, 'Audit receipt'),
        h('p', { className: 'cs-pat-sub' }, 'Local simulation. Nothing was sent or stored outside this preview.'),
        h('ol', null, receipts.map(function (a) { return h('li', { key: a.ref }, h('span', { className: 'cs-pat-strong' }, a.ref), ' ' + a.action + ' ' + a.id + ' (' + a.person + ') at ' + a.at + ' by you' + (a.reason ? '. Reason: ' + a.reason : '') + '.'); }))) : null,
      h(Live, null, live),
      h(C.AlertDialog, {
        open: dialog === 'approve', tone: 'warning', title: 'Approve ' + selected.length + (selected.length === 1 ? ' request?' : ' requests?'), confirmLabel: 'Approve ' + selected.length,
        description: 'These requests on page ' + (pg + 1) + ' will be approved. Requests on other pages are not affected.', onCancel: function () { setDialog(null); }, onConfirm: confirm
      }, h('ul', { className: 'cs-bulk-list' }, selected.map(function (r) { return h('li', { key: r.id }, r.person + ', ' + r.request + ' (' + r.id + ')'); }))),
      h(C.AlertDialog, {
        open: dialog === 'decline', tone: 'danger', title: 'Decline ' + selected.length + (selected.length === 1 ? ' request?' : ' requests?'), confirmLabel: 'Decline ' + selected.length,
        description: 'These requests on page ' + (pg + 1) + ' will be declined with the reason below.', onCancel: function () { setDialog(null); }, onConfirm: confirm
      }, h('div', { className: 'cs-pat-stack' },
        h('ul', { className: 'cs-bulk-list' }, selected.map(function (r) { return h('li', { key: r.id }, r.person + ', ' + r.request + ' (' + r.id + ')'); })),
        h(C.Textarea, { id: base + '-reason', label: 'Reason for declining', required: true, error: reasonError, hint: 'Shared with each person. Applies to every selected request.', maxLength: 300, onChange: function (e) { setReason(e.target.value); if (e.target.value.trim()) setReasonError(''); } }))));
  }

  Object.assign(window.CareSync, { PatternRecordPreview: PatternRecordPreview, PatternEvidenceRegister: PatternEvidenceRegister, PatternGuidedWizard: PatternGuidedWizard, PatternDecisionQueue: PatternDecisionQueue, version: '1.1.0' });
})();
