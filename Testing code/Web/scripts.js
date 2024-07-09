document.getElementById('food-preferences-tab').addEventListener('click', function() {
    document.getElementById('food-preferences').classList.add('active');
    document.getElementById('profile').classList.remove('active');
    this.classList.add('active');
    document.getElementById('profile-tab').classList.remove('active');
    // if click print out something 
});

document.getElementById('profile-tab').addEventListener('click', function() {
    document.getElementById('profile').classList.add('active');
    document.getElementById('food-preferences').classList.remove('active');
    this.classList.add('active');
    document.getElementById('food-preferences-tab').classList.remove('active');
});
