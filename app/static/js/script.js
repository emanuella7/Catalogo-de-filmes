
document.addEventListener('click', function(e) {
  if (e.target.matches('form button.confirm-delete')) {
    if (!confirm("Deseja realmente apagar?")) {
      e.preventDefault();
    }
  }
});

