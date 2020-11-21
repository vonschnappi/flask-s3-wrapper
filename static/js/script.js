function downloadFile(key, fileName) {
    fetch('/download/' + key)
    .then(res => res.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = fileName;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        a.remove()
    });
    
}

function getPath() {
    return window.location.pathname;
}

function bucketListTemplate(data) {
    var html = '<ul>';
    $.each(data, function(index, item){
        html += '<li>'
        html += '<a href="/bucket/' + item +'">' + item + '</a>';
    });
    html += '</ul>';
    return html;
}

function bucketItemListTemplate(bucket, data) {

    var html = '<ul>';
    $.each(data, function(index, item){
        for (let key in item) {
            if (key == 'folders') {
                for (let i in item[key]) {
                    folder = item[key][i];
                    html += '<li><i class="fa fa-folder"></i>&nbsp;<a href="' + 
                    bucket + '/' + folder + '">' + folder + '</a></li>';
                }
            } else {
                for (let i in item[key]) {
                    file = item[key][i];
                    html += '<li><i class="fa fa-file"></i>&nbsp;<a href="' +
                    bucket + '/' + file +'">' + file + '</a>' + 
                    '&nbsp;<button data-file-key-in-bucket="' + bucket + '/' + file + '"' + 
                    'data-file-name="' + file + '"' +
                    'class="download-button">Download ' + file + '</button></li>';
                }
            }
        }
    });
    html += '</ul>';
    return html;
}

function folderItemListTemplate(bucket, folder, data) {
    if (!data[0].folders.length && !data[0].files.length) {
        return '<p> The folder <strong>' + folder + '</strong> is empty.</p>'
    }
    var html = '<ul>';
    $.each(data, function(index, item){
        for (let key in item) {
            if (key == 'folders') {
                for (let i in item[key]) {
                    subFolder = item[key][i];
                    html += '<li><i class="fa fa-folder"></i>&nbsp;<a href="' + 
                    subFolder + '">' + subFolder + '</a></li>';
                }
            } else {
                for (let i in item[key]) {
                    file = item[key][i];
                    html += '<li><i class="fa fa-file"></i>&nbsp;<a href="' +
                    file +'">' + file + '</a>' + 
                    '&nbsp;<button data-file-key-in-bucket="' + bucket + '/' + folder +
                     '/' + file + '"' + 'data-file-name="' + file + '"' +
                    'class="download-button">Download ' + file + '</button></li>';
                }
            }
        }
    });
    html += '</ul>';
    return html;
}

function renderBucketList(data) {
    $('#pagination-container').pagination({
        dataSource: data,
        callback: function(data, pagination) {
            var html = bucketListTemplate(data);
            $('#bucket-list').html(html);
        }
    })
}

function renderBucketItemList(bucket, data) {
    data = [data];
    $('#pagination-container').pagination({
        dataSource: data,
        callback: function(data, pagination) {
            var html = bucketItemListTemplate(bucket, data);
            $('#bucket-list').html(html);
        }
    })
}

function renderFolderItemList(bucket, folder, data) {
    data = [data];
    $('#pagination-container').pagination({
        dataSource: data,
        callback: function(data, pagination) {
            var html = folderItemListTemplate(bucket, folder, data);
            $('#folder-list').html(html);
        }
    })
}

$(document).ready(function() {

    $(".download-button").click(function(){
        var fileKey = $(this).attr('data-file-key-in-bucket');
        var fileName = $(this).attr('data-file-name');
        downloadFile(fileKey, fileName)
    });
    
});