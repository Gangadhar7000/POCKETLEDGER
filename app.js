const form = document.getElementById("transaction-form");
const categorySelect = document.getElementById("category");
const kindInputs = [...document.querySelectorAll('input[name="kind"]')];
const cancelButton = document.getElementById("cancel-edit");
const saveButton = document.getElementById("save-button");

function selectedKind() {
  return kindInputs.find(input => input.checked)?.value || "Expense";
}

function updateCategories(selected = "") {
  const categories = window.TRANSACTION_CATEGORIES[selectedKind()] || [];
  categorySelect.innerHTML = "";
  categories.forEach(category => {
    const option = document.createElement("option");
    option.value = category;
    option.textContent = category;
    if (category === selected) option.selected = true;
    categorySelect.appendChild(option);
  });
}

kindInputs.forEach(input => input.addEventListener("change", () => updateCategories()));
updateCategories();

function openEdit(button) {
  const data = button.dataset;
  form.action = `/edit/${data.id}`;
  document.getElementById("form-heading").textContent = "Edit transaction";
  document.getElementById("title").value = data.title;
  document.getElementById("amount").value = data.amount;
  document.getElementById("transaction_date").value = data.date;
  document.getElementById("note").value = data.note;
  kindInputs.forEach(input => input.checked = input.value === data.kind);
  updateCategories(data.category);
  saveButton.textContent = "Save changes";
  cancelButton.hidden = false;
  document.querySelector(".add-panel").scrollIntoView({ behavior: "smooth", block: "start" });
}

function resetForm() {
  form.reset();
  form.action = "/add";
  document.getElementById("form-heading").textContent = "Add transaction";
  document.getElementById("transaction_date").value = new Date().toISOString().slice(0, 10);
  updateCategories();
  saveButton.textContent = "＋ Add transaction";
  cancelButton.hidden = true;
}

document.querySelectorAll(".flash").forEach(flash => {
  setTimeout(() => flash.classList.add("fade-out"), 4200);
});
