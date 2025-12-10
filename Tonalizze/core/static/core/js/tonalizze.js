document.addEventListener('DOMContentLoaded', () => {
    // Mostra valores dos sliders na tela
    const s1 = document.querySelector('input[name="tonalidade_1"]');
    const s2 = document.querySelector('input[name="tonalidade_2"]');
    const s3 = document.querySelector('input[name="tonalidade_3"]');

    const v1 = document.getElementById('val1');
    const v2 = document.getElementById('val2');
    const v3 = document.getElementById('val3');

    function bindSlider(slider, label) {
        if (!slider || !label) return;
        const update = () => {
            label.textContent = slider.value;
        };
        slider.addEventListener('input', update);
        update();
    }

    bindSlider(s1, v1);
    bindSlider(s2, v2);
    bindSlider(s3, v3);

    // Atalho T para ligar/desligar (apenas visual, no protótipo)
    const bigCircle = document.querySelector('.big-circle');
    const overlay = document.getElementById('filter-overlay');

    if (bigCircle && overlay) {
        document.addEventListener('keydown', (e) => {
            if (e.key === 't' || e.key === 'T') {
                e.preventDefault();
                overlay.classList.toggle('active');
                bigCircle.classList.toggle('active');
                bigCircle.textContent = bigCircle.classList.contains('active') ? 'DESLIGAR' : 'LIGUE AQUI';
            }
        });
    }
});
