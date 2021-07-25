function ShowHide() {
    const elementPane = document.querySelector('.lateralPane');
    var menu = getComputedStyle(elementPane).visibility;

    const elementContainer = document.querySelector('.pageContainer');

    if (menu === "visible") {
        elementPane.style.visibility="hidden";
        elementContainer.style.width="100%";
    }
    else if (menu === "hidden") {
        elementPane.style.visibility="visible";
        elementContainer.style.width="80%";
        document.getElementById('container').style.width="80%";
    }
}

function insertDate(date) {
    var articleDate = document.createElement('p');
    articleDate.innerHTML = date;
    articleDate.setAttribute('class','dateArticle');
    document.getElementsByTagName('P')[0].after(articleDate);
}

function removeAuthorName() {
    document.getElementsByName('thumb').forEach(function (element) {
        if (element.getElementsByTagName('p').length > 1) {
            element.removeChild(element.getElementsByTagName('p').item(1));
        }
    });
}

function removeHTMLBalises() {
    document.getElementsByName('thumb').forEach(function (element) {
        element.innerText.replace(/(<([^>]+)>)/gi, "").replace(/<\/b>/g, "");
    });
}

function copyClipboard() {
    console.log(window.isSecureContent);
    navigator.clipboard.writeText(window.location.href);
    document.execCommand("copy");
    document.getElementById("copyImg").src = "http://mehari-consulting.com/public/img/icons/paste.png";
}