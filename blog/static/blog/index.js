const no_of_contents = document.getElementsByClassName('blogContent').length;
for (let i = 0; i < no_of_contents; i++) {
    if (document.getElementsByClassName('blogContent')[i].innerText.length > 100) {
        let newContent = document.getElementsByClassName('blogContent')[i].innerText.slice(0, 50);
        document.getElementsByClassName('blogContent')[i].innerText = newContent + '...';
    }
}