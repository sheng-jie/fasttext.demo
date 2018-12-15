
<h3>新闻分类器：{{title}}</h3>
<form action="/check" method="post">
    <p>输入新闻</p>
    <textarea name="msg" rows="5" cols="100"> </textarea>
    <br/>
    <input value="检测" type="submit"/>
</form>

<ul>
    % for item in msgs:
        <li>{{item}}</li>
    % end
</ul>
<form action="/clear" method="post">
       
    <input value="清空检测记录" type="submit"/>
</form>
<hr>
