

<!DOCTYPE html>
<html>
<head>
    <meta name="keywords" content="code playground, complier, code editor, interpreter, development, source code, html, css, javascript, js, java, c#, csharp, c++, c, python, php, ruby">
    

    <link rel="shortcut icon" href="/Images/favicon.ico">
    <link rel="icon" type="image/png" href="/Images/favicon-192x192.png" sizes="192x192" style="background-color: white;">
    <link rel="apple-touch-icon" sizes="180x180" href="/Images/favicon-180x180.png" style="background-color: white;">

        <link href="/Styles/compiler?v=LjZ2BETj4t1IvsQgHz713WNPsedUvf5k2st2Ddhhhws1" rel="stylesheet"/>

        <script src="/bundles/jquery?v=yMmPM1TxecYcoWtCWW3jYgH0fr9kiAasOfb-W5I001A1"></script>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.3.0/ace.js" type="text/javascript" charset="utf-8"></script>
        <script src="https://ajaxorg.github.io/ace-builds/src/ext-language_tools.js" type="text/javascript" charset="utf-8"></script>    
     <script src="/Scripts/compiler?v=vjaMtToDg1bepn9LxhYlyq1gL1IYkKj2Rei7DDrlFlo1"></script>

    <script>
        window.userId = 0;
        window.isLogged = window.userId > 0;
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
    
        <title>Start of 3D vector class | Code Playground</title>
        <meta name="description" content="Check out my code on SoloLearn">

        <meta property="og:site_name" content="SoloLearn">
        <meta property="og:title" content="Start of 3D vector class">
        <meta property="og:description" content="Check out what Andres Preciado has created on SoloLearn">
        <meta property="og:image" content="https://www.sololearn.com/Icons/Avatars/10396498.jpg" />
        <meta property="og:locale" content="en_us">
        <meta property = "og:url" content = "https://code.sololearn.com/cck0VuERXsOD/">
        <meta property="fb:app_id" content="153040644900826">

</head>
<body>

    



        <script>
            window.isUserCode = true;
            window.language = "py";
            window.publicId = "cck0VuERXsOD";
            window.alias = "Python";
            window.codeName = "Start of 3D vector class";
            window.codeUserId = 10396498;
            window.codeId = 4546342;
            window.isPublic = false;
            window.isMyCode = false;
        </script>
        <script>
            window.isCodeTemplate = true;
        </script>
    <script>
        window.code = "class Vector3D:\n\tdef __init__(self, x, y, z):\n\t\tself.x = x\n\t\tself.y = y\n\t\tself.z = z\n\tdef __add__(self, other):\n\t\treturn Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)\n\nfirst = Vector3D(5, 7, 2)\nsecond = Vector3D(3, 9, 8)\nresult = first + second\nprint(result.x)\nprint(result.y)\nprint(result.z)\n";
        window.cssCode = "";
        window.jsCode = "";
    </script>


<div id="playgroundContainer" data-id="4546342" class="userCode">
    <div id="header">
    <div class="wrapper">
        <div class="sandwichButton"></div>
        <div class="logo">
            <a href="https://www.sololearn.com/" target="_blank">
                <svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                     viewBox="0 0 330 60" enable-background="new 0 0 330 60" xml:space="preserve">
                <g>
                <g>
                <g>
                <g>
                <path fill="#FDFDFE" d="M120.8,4c-6.8,2.2-13.9,8.4-13,15.4c0,8,8,14.2,15.9,16.8c-6.2-7.1-10.6-15.9-6.7-25.6
					                    C118.8,6.5,120.8,4,120.8,4z" />
			                    </g>
                <g>
                <path fill="#FDFDFE" d="M106.1,21.3c-2.7,7-0.1,15.8,5.2,19.4c7.1,5.3,16.8,2.7,23.9-3.5c-9.7,1.8-20.3,0-25.7-8.7
					                    C107.1,24.4,106.1,21.3,106.1,21.3z" />
			                    </g>
                <g>
                <path fill="#FDFDFE" d="M112.5,43.4c4.9,6,13.8,8.5,20.9,5.8c4.8-1.9,8.4-7.1,9.2-13c0.5-3-0.1-5.5-0.5-8.5
					                    c-3.5,9.7-11.4,16.5-21.6,17C115.8,44.4,112.5,43.4,112.5,43.4z" />
			                    </g>
                <g>
                <path fill="#FDFDFE" d="M136.4,49.6c7.7-1.9,15.6-9,15.6-16.9c0-5.3-5.5-14.8-15.9-16.8c7.1,7.1,11.5,18.6,5.4,27.5
					                    C138.8,47.3,136.4,49.6,136.4,49.6z" />
			                    </g>
                <g>
                <path fill="#FDFDFE" d="M153.5,30.5c1.1-7.6-0.7-17.3-7.7-20.9c-4.4-2.7-17.3-0.1-21.2,7.1c8.9-3.5,20.3-2.7,25.7,6.8
					                    C152.6,27.4,153.5,30.5,153.5,30.5z" />
			                    </g>
                <g>
                <path fill="#FDFDFE" d="M144.3,7.1c-5.6-4.5-14.4-7.1-20.6-2.7c-7.1,4.4-8.8,14.1-4.4,22.1c0.9-9.7,8-17.7,17.4-19.4
					                    C141.1,6.6,144.3,7.1,144.3,7.1z" />
			                    </g>
		                    </g>
                <g>
                <path fill="#FDFDFE" d="M24.4,37.1c0-1.8-0.7-3.3-2-4.6c-1.3-1.2-3.6-2.3-6.9-3.1c-4.1-1-7.3-2.5-9.6-4.5c-2.3-2-3.4-4.4-3.4-7.4
				                    c0-3.1,1.2-5.8,3.7-7.9c2.5-2.1,5.7-3.1,9.6-3.1c4.2,0,7.6,1.2,10.1,3.6c2.5,2.4,3.7,5.2,3.7,8.4l-0.1,0.2h-5.2
				                    c0-2.3-0.8-4.2-2.4-5.7c-1.6-1.5-3.6-2.2-6.1-2.2c-2.5,0-4.5,0.6-5.8,1.8c-1.4,1.2-2,2.8-2,4.8c0,1.7,0.7,3.2,2.2,4.4
				                    c1.5,1.2,3.9,2.2,7.2,3.1c4,1,7.1,2.6,9.2,4.6c2.1,2,3.2,4.6,3.2,7.6c0,3.2-1.3,5.8-3.8,7.8c-2.5,2-5.9,2.9-10,2.9
				                    c-3.9,0-7.3-1.1-10.3-3.3c-3-2.2-4.4-5.1-4.3-8.7l0.1-0.2h5.2c0,2.5,1,4.5,2.9,5.8c1.9,1.4,4.1,2.1,6.5,2.1
				                    c2.6,0,4.6-0.6,6.1-1.7C23.6,40.6,24.4,39.1,24.4,37.1z" />
                <path fill="#FDFDFE" d="M68.1,30.7c0,4.9-1.5,9-4.6,12.2c-3,3.2-7,4.9-11.8,4.9c-4.7,0-8.5-1.6-11.4-4.9
				                    c-2.9-3.2-4.4-7.3-4.4-12.2v-7.1c0-4.9,1.5-9,4.4-12.2c2.9-3.3,6.7-4.9,11.4-4.9c4.9,0,8.8,1.6,11.8,4.9c3,3.2,4.6,7.3,4.6,12.2
				                    V30.7z M62.7,23.5c0-3.7-1-6.7-3-9c-2-2.4-4.6-3.5-8-3.5c-3.2,0-5.7,1.2-7.6,3.5c-1.9,2.4-2.8,5.4-2.8,9v7.2
				                    c0,3.7,0.9,6.7,2.8,9.1c1.9,2.4,4.4,3.5,7.6,3.5c3.4,0,6-1.2,8-3.5c2-2.3,3-5.4,3-9.1V23.5z" />
                <path fill="#FDFDFE" d="M81.4,43H101v4.2H76V7.1h5.4V43z" />
                <path fill="#FDFDFE" d="M168.6,43h19.6v4.2h-25V7.1h5.4V43z" />
                <path fill="#FDFDFE" d="M216.1,28.6h-16.5V43h19.3v4.2h-24.7V7.1h24.4v4.3h-19v13h16.5V28.6z" />
                <path fill="#FDFDFE" d="M246,36.9h-15.1l-3.6,10.3h-5.5l14.5-40.1h4.7l14.2,40.1h-5.5L246,36.9z M232.5,32.3h12l-5.8-17.2h-0.2
				                    L232.5,32.3z" />
                <path fill="#FDFDFE" d="M266.4,29.8v17.4H261V7.1h13.7c4.4,0,7.7,1,10.1,2.9c2.3,1.9,3.5,4.8,3.5,8.5c0,2.1-0.5,3.9-1.6,5.4
				                    c-1.1,1.5-2.6,2.7-4.7,3.6c2.2,0.7,3.8,1.9,4.8,3.5c1,1.6,1.4,3.6,1.4,6v3.8c0,1.2,0.1,2.4,0.4,3.4c0.3,1,0.8,1.8,1.4,2.4v0.7
				                    h-5.6c-0.7-0.6-1.2-1.5-1.4-2.8c-0.2-1.2-0.3-2.5-0.3-3.7V37c0-2.2-0.6-3.9-1.9-5.2c-1.3-1.3-3-2-5.1-2H266.4z M266.4,25.5h7.7
				                    c3.1,0,5.3-0.6,6.6-1.8c1.3-1.2,2-2.9,2-5.3c0-2.3-0.7-4-2-5.3c-1.3-1.2-3.4-1.9-6.1-1.9h-8.3V25.5z" />
                <path fill="#FDFDFE" d="M327.3,47.2h-5.4l-19.3-30.7l-0.2,0.1v30.6h-5.4V7.1h5.4l19.3,30.6l0.2-0.1V7.1h5.4V47.2z" />
		                    </g>
	                    </g>
                    </g>
               
                </svg>
            </a>
        </div>
        <div class="navigation-menu">
            <ul class="Playground">
                <!-- Getting From DB -->
                <li id="courses">
                    <a href="https://www.sololearn.com/Courses/" target="_blank">COURSES</a>
                </li>
                <li id="codes" class="active">
                    <a href="https://www.sololearn.com/Codes/" target="_blank">CODE PLAYGROUND</a>
                </li>
                <li id="discuss">
                    <a href="https://www.sololearn.com/Discuss/" target="_blank">DISCUSS</a>
                </li>
                <li id="leaders">
                    <a href="https://www.sololearn.com/Leaderboard/" target="_blank">TOP LEARNERS</a>
                </li>
                <li id="blogPage">
                    <a href="https://www.sololearn.com/Blog/" target="_blank">BLOG</a>
                </li>
                <li class="signin" data-id="">
                    <a href="https://www.sololearn.com/Profile/" target="_blank">SIGN IN</a>
                </li>
            </ul>
        </div>
    </div>
</div>

<form action="/RedirectToLogin" id="saveForm" method="post"><input class="saveSourceCode" id="Code" name="Code" type="hidden" value="class Vector3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	def __add__(self, other):
		return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

first = Vector3D(5, 7, 2)
second = Vector3D(3, 9, 8)
result = first + second
print(result.x)
print(result.y)
print(result.z)
" /><input class="saveCssCode" id="CssCode" name="CssCode" type="hidden" value="" /><input class="saveJsCode" id="JsCode" name="JsCode" type="hidden" value="" /><input class="saveLanguage" id="Language" name="Language" type="hidden" value="py" /><input id="PublicId" name="PublicId" type="hidden" value="cck0VuERXsOD" /></form>    
    <div id="topToolbar">
        <div class="actions"></div>
        <div class="webActions">
            <button class="tab-box" data-type="web" data-editor="html" alias="html">HTML</button>
            <button class="tab-box" data-type="web" data-editor="css" alias="css">CSS</button>
            <button class="tab-box" data-type="web" data-editor="javascript" alias="js">JS</button>
        </div>
        <div class="defaultActions">
            <button class="tab-box" data-type="default" data-editor=""></button>
        </div>
        <div class="headerTab">
            <button class="tab-box active">Output</button>
        </div>
    </div>

    <div id="editorContainer">
        <div id="editor"></div>

        <div id="output">
            <div class="defaultOutput"></div>

            <div class="webOutput">
                <iframe id="outputFrame" frameborder="0"></iframe>
            </div>
        </div>
    </div>

    <div id="bottomToolbar">
        <div class="wide left">
            <div class="right">
                <div class="cell right">
                    <button class="resetCode">RESET</button>
                    <button class="runCode">RUN</button>
                </div>
                <div class="cell right">
                    <button class="save">SAVE</button>
                    <button class="saveas">SAVE AS</button>
                </div>
            </div>
        </div>
        <div id="jsConsole" class="right">
            <label>JavaScript Console</label>
            <div class="logMessage">

            </div>
            <div class="errorMessage">

            </div>
        </div>
        <div id="badges" class="right">
            <a href="https://play.google.com/store/apps/developer?id=SoloLearn" target="_blank" class="learnOnAndroid">
                <div class="googlePlayBadge"></div>
            </a>
            <a href="https://itunes.apple.com/us/developer/sololearn-inc/id933957049" target="_blank" class="learnOnIOS">
                <div class="appStoreBadge"></div>
            </a>
        </div>
    </div>

        <div class="codeDetails">
            <div class="content">
                <div class="vote centered">
                    <div class="upvote " data-value="1"></div>
                    <p class="">0</p>
                    <div class="downvote " data-value="-1"></div>
                </div>
                <a class="avatar" href="https://www.sololearn.com/Profile/10396498" target="_blank">
                    <img src="/Icons/Avatars/10396498.jpg" title="Andres Preciado" alt="Andres Preciado">
                </a>
                <div class="text">
                    <p class="codeName">Start of 3D vector class</p>
                </div>
            </div>
        </div>

    <div class="settings left">
        <div class="themeContainer">
            <div class="themeSelector">
                <div data-theme="monokai" class="active theme">Dark</div>
                <div data-theme="crimson_editor" class="theme">Light</div> 
            </div>
        </div>
        <div class="languageSelector">
            <select>
                <option value="html" data-type="web" data-editor="html">HTML/CSS/JS</option>
                <option value="js" data-type="webJquery" data-editor="javascript">jQuery</option>
                <option value="cpp" data-type="default" data-editor="c_cpp" alias="cpp">C++</option>
                <option value="c" data-type="default" data-editor="c" alias="c">C</option>
                <option value="cs" data-type="default" data-editor="csharp" alias="cs">C#</option>
                <option value="java" data-type="default" data-editor="java" alias="java">Java</option>
                <option value="py" data-type="default" data-editor="python" alias="py">Python 3</option>
                <option value="php" data-type="combined" data-editor="php" alias="php">PHP</option>
                <option value="rb" data-type="default" data-editor="ruby" alias="rb">Ruby</option>
                <option value="kt" data-type="default" data-editor="kotlin" alias="kt">Kotlin</option>
                <option value="swift" data-type="default" data-editor="swift" alias="swift">Swift</option>
            </select>
        </div>
    </div>

    <div class="share">
        <span>SHARE</span>
        <div class="shareButton"></div>
    </div>
</div>

<div class="loadingOverlay">
    <div class="loadingWrapper">
        <div class="popup">
            <div class="saveLoading"></div>
        </div>
    </div>
</div>

    <script type="text/javascript" src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-5720d15c98e6f544"></script>

    <script type="text/javascript">
        var addthis_config = addthis_config || {};
        addthis_config.data_track_addressbar = false;
        addthis_config.data_track_clickback = false;
    </script>
    <script>
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date(); a = s.createElement(o),
            m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

        ga('create', 'UA-42641357-2', 'auto');
        ga('require', 'displayfeatures');
        ga('send', 'pageview');
    </script>
</body>
</html>