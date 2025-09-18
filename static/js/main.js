
function not_available() {
  Swal.fire({
  imageUrl: "static/img/n_disponivel_img.png",
  imageHeight: 500,
  imageAlt: "(Em breve) Ainda não disponivel"
  });
}

function confirmar_pedido() {
  const btn = document.getElementById("btn-finalizar");
  const url = btn.getAttribute("data-url");

  Swal.fire({
    title: "Tem certeza que deseja finalizar?",
    text: "Não é possível reverter isso",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sim, Finalizar",
    cancelButtonText: "Cancelar"
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: "Pedido efetuado",
        text: "seu pedido foi realizado com sucesso!",
        icon: "success"
      }).then (() => {
        window.location.href = url;
      });
    }
  });
}