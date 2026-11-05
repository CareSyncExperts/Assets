/* Care Sync Hub: the one settings registry used by the design boards.
   Every rule is defined once here (mirroring the super admin "Rules and promises" screen, board 80).
   Boards read values with CSR.get('id', fallback). The Rules board can save trial changes in this
   browser (localStorage key "csRegistryTrial"), so other boards show the change when reopened.
   If storage is blocked, the defaults below are used. */
(function () {
  var D = {
    // Promises and timings
    'weekly-update-day': 'Friday',
    'weekly-update-time': '16:00',
    'weekly-rhythm': 'Monday review, Wednesday chase, Thursday second-person check, Friday send',
    'reply-client': '1 working day',
    'reply-senior': '2 working hours',
    'intro-call': '2 working hours',
    'working-hours': '09:00 to 17:30, Monday to Friday',
    'bank-holidays': 'England and Wales, or Northern Ireland, by the client\'s nation',
    'quiet-hours': '8pm to 8am',
    'send-after-signing': '2 working days',
    // Alerts and thresholds
    'no-contact-red-days': 7,
    'unanswered-red': '1 working day',
    'watch-gap-red-days': 7,
    'waiting-amber-days': 5,
    'waiting-red-days': 10,
    // Reminders
    'form-reminders': 'after 2 days and 4 days; Grace calls on day 6; then weekly',
    'document-reminders': 'after 3 days, then weekly',
    'third-party-reminders': 'after 3 working days, then weekly',
    'signature-reminders': 'after 2 days, then the consultant calls',
    'expiry-warning-weeks': 6,
    // Journey and sessions
    'sessions-included': 3,
    'session-length': '1 hour',
    'aftercare-months': 12,
    'aftercare-packages': 'Full start-up package only (others can buy it as an add-on)',
    'inspection-readiness-month': 4,
    'cv-gap-weeks': 4,
    // Regulators (legal values are shown, not edited)
    'nop-legal-days': 28,
    'nop-draft-day': 14,
    'nop-review-day': 20,
    'nop-send-day': 21,
    'rfi-target-days-before': 4,
    // Tenders
    'tender-submit-days-before': 2,
    'tender-draft-days-before': 10,
    'tender-approve-days-before': 5,
    // Weekends: an internal target that falls on a weekend or bank holiday moves to the working day before
    'target-weekend-rule': 'the working day before',
    // Legal identity (open decision: shown on the client Security page once set)
    'ico-number': '',
    // Security
    'break-glass-hours': 4,
    'staff-idle-timeout': '30 minutes',
    'client-device-days': 30,
    'staff-absolute-timeout': '10 hours',
    'vault-reveal-threshold': 15,
    'export-link-hours': 24,
    // More limits (from the registry, board 80)
    'growth-ideas-per-month': 1,
    'document-review-reminder': 'after 3 days',
    'refs-max-age-months': 6,
    'dbs-max-age-months': 12,
    'address-history-years': 5,
    'tender-tight-days': 15,
    'unusual-exports-per-day': 5,
    'link-expiry-days': 14,
    'upload-max-mb': 20,
    'vault-reveal-seconds': 30,
    'complaint-ack': '1 working day',
    'complaint-reply-days': 20,
    'price-aftercare-addon': '',
    'price-extra-session': '',
    // Reviews
    'review-platforms': 'Google and Trustpilot',
    'review-reminder-days': 7,
    // Money
    'vat-rate': 20,
    'payment-provider': 'Stripe',
    'price-dom': 4000, 'price-sl': 5000, 'price-full': 8500, 'price-ciw': 4500, 'price-rqia': 4500,
    'price-sl-addon': 1500, 'price-interview': 750, 'price-pir': 750, 'price-tender-from': 1500
  };
  var T = {};
  try { T = JSON.parse(window.localStorage.getItem('csRegistryTrial') || '{}') || {}; } catch (e) { T = {}; }
  window.CSR = {
    defaults: D,
    trial: T,
    get: function (id, fallback) {
      if (Object.prototype.hasOwnProperty.call(T, id)) return T[id];
      if (Object.prototype.hasOwnProperty.call(D, id)) return D[id];
      return fallback;
    },
    setTrial: function (id, value) {
      T[id] = value;
      try { window.localStorage.setItem('csRegistryTrial', JSON.stringify(T)); } catch (e) {}
    },
    clearTrial: function () {
      T = {}; this.trial = T;
      try { window.localStorage.removeItem('csRegistryTrial'); } catch (e) {}
    },
    money: function (n) { return '£' + Number(n).toLocaleString('en-GB'); }
  };
})();
