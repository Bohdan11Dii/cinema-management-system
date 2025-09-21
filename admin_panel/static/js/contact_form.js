document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('formset-container');
    const addBtn = document.getElementById('add-contact');
    const emptyFormEl = document.getElementById('empty-form');
    const emptyFormHtml = emptyFormEl ? emptyFormEl.innerHTML : '';
    const totalFormsInput = container.querySelector('input[name$="TOTAL_FORMS"]');
    const maxFormsInput = container.querySelector('input[name$="MAX_NUM_FORMS"]');

    if (!container || !addBtn || !emptyFormEl || !totalFormsInput) {
        console.warn('Formset JS: не знайдено потрібні елементи.');
        return;
    }

    function updateIndices() {
        const forms = container.querySelectorAll('.contact-form');
        forms.forEach((formEl, i) => {
            formEl.querySelectorAll('input, select, textarea, label').forEach(el => {
                if (el.name) el.name = el.name.replace(/-\d+-/, `-${i}-`);
                if (el.id) el.id = el.id.replace(/-\d+-/, `-${i}-`);
                if (el.htmlFor) el.htmlFor = el.htmlFor.replace(/-\d+-/, `-${i}-`);
            });
        });
        totalFormsInput.value = forms.length;
    }

    function bindRemoveButton(btn) {
        if (!btn || btn.dataset.bound) return;
        btn.dataset.bound = '1';
        btn.addEventListener('click', () => {
            const formEl = btn.closest('.contact-form');
            const deleteInput = formEl.querySelector(`input[type="checkbox"][name$="-DELETE"]`);
            if (deleteInput) {
                deleteInput.checked = true;
                formEl.style.display = 'none';
            } else {
                formEl.remove();
            }
            updateIndices();
        });
    }

    container.querySelectorAll('.remove-form').forEach(btn => bindRemoveButton(btn));

    addBtn.addEventListener('click', () => {
        const currentCount = parseInt(totalFormsInput.value, 10);
        if (maxFormsInput && maxFormsInput.value && currentCount >= parseInt(maxFormsInput.value, 10)) {
            alert('Досягнуто максимальної кількості форм');
            return;
        }
        const newHtml = emptyFormHtml.replace(/__prefix__/g, currentCount);
        container.insertAdjacentHTML('beforeend', newHtml);
        const newForm = container.querySelectorAll('.contact-form')[container.querySelectorAll('.contact-form').length - 1];
        bindRemoveButton(newForm.querySelector('.remove-form'));
        updateIndices();
    });
});
