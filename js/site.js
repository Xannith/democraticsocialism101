/* Progressive enhancement only. The site is fully usable without JavaScript.
   Marks the current page in the nav and footer with aria-current for
   orientation and keyboard clarity. ASCII hyphens only, no en or em dashes. */
(function () {
  "use strict";

  var path = window.location.pathname;
  if (path.length > 1 && path.charAt(path.length - 1) === "/") {
    path = path + "index.html";
  }

  var links = document.querySelectorAll(".site-nav__list a, .footer-nav a");
  for (var i = 0; i < links.length; i++) {
    var href = links[i].getAttribute("href");
    if (!href) {
      continue;
    }
    if (href.charAt(href.length - 1) === "/") {
      href = href + "index.html";
    }
    if (href === path) {
      links[i].setAttribute("aria-current", "page");
    }
  }
})();
