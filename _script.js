<script type="text/javascript">

{

function resizeFrames()
var framesList = document.getElementsByTagName('iframe');
for (var i = 0; i < framesList.length; i++)try {


objToResize.height = innerDoc.body.scrollHeight + 10;

objToResize.width = innerDoc.body.scrollWidth;
}
{

var frame = framesList[i];var innerDoc = (frame.contentDocument) ? frame.contentDocument : frame.contentWindow.document;var objToResize = (frame.style) ? frame.style : frame;catch (err)// Do nothing

}
}
</script>
