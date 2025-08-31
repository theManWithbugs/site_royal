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

const ctxPedidos = document.getElementById('chartPedidos');
new Chart(ctxPedidos, {
    type: 'doughnut',
    data: {
        labels: ['Concluídos', 'Pendentes', 'Cancelados'],
        datasets: [{
            data: [90, 25, 10],
            backgroundColor: ['#dc3545', '#ffc107', '#6c757d']
        }]
    },
    options: { responsive: true }
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
