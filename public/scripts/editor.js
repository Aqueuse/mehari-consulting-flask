function addImgTag(img) {
    let textArea = document.getElementById('articleAreaId');
    textArea.focus();

    let oldTextContent = textArea.value;
    let cursorPosition = textArea.selectionStart;

    let beforeCursorText = oldTextContent.substring(0, cursorPosition);
    let afterCursorText = oldTextContent.substring(cursorPosition, oldTextContent.length);

    let newTextContent = beforeCursorText + " <img src='" + img + "'> " + afterCursorText;

    textArea.value = newTextContent;
}

function copyImagesList() {
    let content = document.getElementById("articleAreaId").value;

    let articleContent = document.createElement('div');
    articleContent.setAttribute('id', 'articlePreview');
    articleContent.setAttribute('style', "display:none");

    articleContent.innerHTML = content;
    document.body.append(articleContent);

    let imagesList = Array.from(document.getElementById('articlePreview').getElementsByTagName('img'));

    let imageItem;
    if (imagesList.length === 0) {
        imageItem = document.createElement('input');
        imageItem.setAttribute('type', 'text');
        imageItem.setAttribute('name', 'image');
        imageItem.setAttribute('value', 'defaultIMG.jpg');
            if (document.getElementById('formCreateArticle') != null)
                imageItem = document.getElementById('formCreateArticle').append(imageItem);
            if (document.getElementById('formEditArticle') != null)
                imageItem = document.getElementById('formEditArticle').append(imageItem);
    }
    else {
        imagesList.forEach(element => {
            let imgSource = element.src.split('/')[(element.src.split('/').length) - 1];
            imageItem = document.createElement('input');
            imageItem.setAttribute('type', 'text');
            imageItem.setAttribute('name', 'image');
            imageItem.setAttribute('value', imgSource);
            if (document.getElementById('formCreateArticle') != null)
                imageItem = document.getElementById('formCreateArticle').append(imageItem);
            if (document.getElementById('formEditArticle') != null)
                imageItem = document.getElementById('formEditArticle').append(imageItem);
        });
    }
}

function switchPane(paneID) {
    if (paneID == 'img_unused') {
        document.getElementById('img_unused').style.display = "block";
        document.getElementById('img_unused').style.backgroundColor = "gray";
        document.getElementById('img_unused_btn').style.backgroundColor = "gray";

        document.getElementById('img_by_article').style.display = "none";
        document.getElementById('img_by_article_btn').style.backgroundColor = "lightgray";
    }
    if (paneID == 'img_by_article') {
        document.getElementById('img_by_article').style.display = "block";
        document.getElementById('img_by_article').style.backgroundColor = "gray";
        document.getElementById('img_by_article_btn').style.backgroundColor = "gray";

        document.getElementById('img_unused').style.display = "none";
        document.getElementById('img_unused_btn').style.backgroundColor = "lightgray";
    }
}