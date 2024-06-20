document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.querySelector(".navbar-toggler");
  const sidebar = document.getElementById("sidebar");

  toggleButton.addEventListener("click", function () {
    sidebar.classList.toggle("show");
  });

  document.addEventListener("click", function (event) {
    if (
      !sidebar.contains(event.target) &&
      !toggleButton.contains(event.target)
    ) {
      sidebar.classList.remove("show");
    }
  });
});
