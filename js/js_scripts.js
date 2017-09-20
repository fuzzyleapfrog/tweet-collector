function ValidURL(url) {
    if((url.search("http://twitter.com/") == 0
     || url.search("https://twitter.com/") == 0)
     && url.search("/status/") != -1) {
        return true;
    } else {
        return false;
    }
}

function myFunction() {
    var url, text;

    url = document.getElementById("url").value;

    if (!ValidURL(url)) {
        document.getElementById("space").innerHTML = "";
        text = "This is not a link to a tweet!";
        document.getElementById("response negative").innerHTML = text;
    } else {
        document.getElementById("space").innerHTML = "";
        text = "Tweet has been collected!";
        // TODO: Collect tweet
	// TODO: Check whether it allready exists in the database
	// TODO: Replace background colour of the text depending an ValidURL
        document.getElementById("response positive").innerHTML = text;
    }
}
