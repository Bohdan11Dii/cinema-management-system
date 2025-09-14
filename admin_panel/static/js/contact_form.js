document.addEventListener('DOMContentLoaded', () => {
    const prefix = "contacts";  // має збігатися з prefix у view
    const addBtn = document.getElementById('add-contact');
    const container = document.getElementById('formset-container');
    const emptyFormEl = document.getElementById('empty-form');
    const emptyFormHtml = emptyFormEl ? emptyFormEl.innerHTML : '';
    const totalFormsInput = document.getElementById(`id_${prefix}-TOTAL_FORMS`);
    const maxFormsInput = document.getElementById(`id_${prefix}-MAX_NUM_FORMS`);

    if (!totalFormsInput) {
        console.error('Management form не знайдено! Перевір template та prefix.');
        return;
    }

    // Функція оновлення індексів і TOTAL_FORMS
    function updateIndices() {
        const forms = container.querySelectorAll('.contact-form');
        forms.forEach((formEl, i) => {
            formEl.querySelectorAll('input, select, textarea, label').forEach(el => {
                if (el.name) el.name = el.name.replace(new RegExp(`${prefix}-\\d+-`), `${prefix}-${i}-`);
                if (el.id) el.id = el.id.replace(new RegExp(`${prefix}-\\d+-`), `${prefix}-${i}-`);
                if (el.htmlFor) el.htmlFor = el.htmlFor.replace(new RegExp(`${prefix}-\\d+-`), `${prefix}-${i}-`);
            });
        });
        totalFormsInput.value = forms.length;
    }

    // Функція прив’язки видалення до кнопки
    function bindRemoveButton(btn) {
        if (!btn || btn.dataset.bound) return;
        btn.dataset.bound = '1';
        btn.addEventListener('click', () => {
            const formEl = btn.closest('.contact-form');
            const deleteInput = formEl.querySelector(`input[name$="-DELETE"]`);
            if (deleteInput) {
                // існуюча форма з БД — позначаємо DELETE і ховаємо
                deleteInput.checked = true;
                formEl.style.display = 'none';
                updateIndices();
            } else {
                // нова форма — просто видаляємо
                formEl.remove();
                updateIndices();
            }
        });
    }

    // Прив’язка видалення до всіх існуючих кнопок
    container.querySelectorAll('.contact-form .remove-form').forEach(btn => bindRemoveButton(btn));

    // Додавання нової форми
    addBtn.addEventListener('click', () => {
        const currentCount = parseInt(totalFormsInput.value, 10);
        if (maxFormsInput && maxFormsInput.value && currentCount >= parseInt(maxFormsInput.value, 10)) {
            alert('Досягнуто максимальної кількості форм');
            return;
        }

        // Створюємо нову форму з empty_form
        const newHtml = emptyFormHtml.replace(/__prefix__/g, currentCount);
        container.insertAdjacentHTML('beforeend', newHtml);

        // Прив’язуємо видалення до нової кнопки
        const newFormEl = container.querySelectorAll('.contact-form')[container.querySelectorAll('.contact-form').length - 1];
        const newBtn = newFormEl.querySelector('.remove-form');
        bindRemoveButton(newBtn);

        updateIndices();
    });
});
