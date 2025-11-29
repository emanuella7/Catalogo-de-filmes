// Se você quiser usar confirmação por JS para todos os forms de exclusão,
// pode adicionar atributo data-confirm="true" ao form e usar este script.
// Atualmente as páginas de confirmação usam página separada, então este é opcional.
document.addEventListener('click', function(e) {
  if (e.target.matches('form button.confirm-delete')) {
    if (!confirm("Deseja realmente apagar?")) {
      e.preventDefault();
    }
  }
});
