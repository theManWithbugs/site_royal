const ctxVendas = document.getElementById('chartVendas');
new Chart(ctxVendas, {
    type: 'line',
    data: {
        labels: ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
        datasets: [{
            label: 'Vendas',
            data: [200, 180, 190, 220, 300, 350, 400],
            borderColor: '#dc3545',
            backgroundColor: 'rgba(220,53,69,0.2)',
            fill: true
        }]
    },
    options: { responsive: true, plugins: { legend: { display: false } } }
});


document.addEventListener('DOMContentLoaded', function() {
  const title = document.title.trim();
  const texto_navbar = document.getElementById('texto_navbar');

  if (title === 'HOME |') {
    texto_navbar.textContent = 'Painel Royal';
  } else if (title === 'HOME | INVESTIMENTOS') {
    texto_navbar.textContent = 'Investimentos Royal';
  }
})

fetch('/admin_royal/response_invest/')
    .then(response => {
        if (window.chartDrawn) return;
        window.chartDrawn = true;
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
      console.log(data.data);

      const ctxPedidos = document.getElementById('chartPedidos');
      new Chart(ctxPedidos, {
          type: 'doughnut',
          data: {
              labels: ['Wilian', 'Victor'],
              datasets: [{
                  data: [90, 25],
                  backgroundColor: ['#dc3545', '#ffc107']
              }]
          },
          options: { responsive: true }
      });
    })
    .catch(error => console.error('Erro:', error));