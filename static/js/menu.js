 toggled = true;

function openMenu() {
  if (toggled) {
    document.getElementById("right").style.display = "flex";
    console.log("oui");
    toggled = !toggled;
  } else {
    document.getElementById("right").style.display = "none";
    toggled = !toggled;
  }
}
