// Вибір елементів
const openIncomeModalButton = document.getElementById("open-income-modal");
const openExpenseModalButton = document.getElementById("exp-btn");

const incomeModal = document.getElementById("income-modal");
const expenseModal = document.getElementById("expense-modal");

const closeIncomeModalButton = document.getElementById("close-income-modal"); // У вас може бути той самий ID для двох хрестиків. Змінімо це.
const closeExpenseModalButton = document.getElementById("close-expense-modal");

// Відкриття модальних вікон
openIncomeModalButton.addEventListener("click", () => {
    incomeModal.style.display = "block";
});

openExpenseModalButton.addEventListener("click", () => {
    expenseModal.style.display = "block";
});

// Закриття модальних вікон
closeIncomeModalButton.addEventListener("click", () => {
    incomeModal.style.display = "none";
});

closeExpenseModalButton.addEventListener("click", () => {
    expenseModal.style.display = "none";
});

// Закриття при натисканні поза модальним вікном
window.addEventListener("click", (event) => {
    if (event.target === incomeModal) {
        incomeModal.style.display = "none";
    }
    if (event.target === expenseModal) {
        expenseModal.style.display = "none";
    }
});
