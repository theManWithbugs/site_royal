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
  } else if (title === 'HOME | REG-ITEMS') {
    texto_navbar.textContent = 'Registrar Produtos';
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
        // console.log(data.data);

        // data.data.forEach(dados => {
        //     console.log(dados.nome);
        // })

        let user_0 = data.data[0];
        let user_1 = data.data[1];

        const ctxPedidos = document.getElementById('chartPedidos');
        new Chart(ctxPedidos, {
            type: 'doughnut',
            data: {
                labels: [user_0["nome"], user_1["nome"]],
                datasets: [{
                    data: [user_0["total"], user_1["total"]],
                    backgroundColor: ['#dc3545', '#ffc107']
                }]
            },
            options: { responsive: true }
        });
    })
    .catch(error => console.error('Erro:', error));

fetch('/admin_royal/response_titulo/')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {

        box = document.getElementById('box');

        ul = document.createElement('ul');
        ul.classList.add('list-group');
        data.forEach(item => {
            li = document.createElement('li');
            li.textContent = `INVESTIDOR: ${item.nome.toUpperCase()} | INVESTIMENTO: ${item.titulo} | VALOR: ${item.total}`;
            li.classList.add('list-group-item');
            ul.appendChild(li);
        });
        box.appendChild(ul);
    })
    .catch(error => console.error('Erro:', error));
