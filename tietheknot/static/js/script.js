document.addEventListener('DOMContentLoaded', function () {
    var sideNavbar = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sideNavbar);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.modal');
    M.Modal.init(elems);
});