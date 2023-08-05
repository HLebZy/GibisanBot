<!doctype html>
<html lang="ru" dir="ltr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="referrer" content="no-referrer">
  <meta name="robots" content="noindex,nofollow">
  <style id="cfs-style">html{display: none;}</style>
  <link rel="icon" href="favicon.ico" type="image/x-icon">
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <link rel="stylesheet" type="text/css" href="./themes/bootstrap/jquery/jquery-ui.css">
  <link rel="stylesheet" type="text/css" href="js/vendor/codemirror/lib/codemirror.css?v=5.2.0">
  <link rel="stylesheet" type="text/css" href="js/vendor/codemirror/addon/hint/show-hint.css?v=5.2.0">
  <link rel="stylesheet" type="text/css" href="js/vendor/codemirror/addon/lint/lint.css?v=5.2.0">
  <link rel="stylesheet" type="text/css" href="./themes/bootstrap/css/theme.css?v=5.2.0">
  <title>phpMyAdmin</title>
    <script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.min.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery-migrate.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/sprintf.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/ajax.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/keyhandler.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery-ui.min.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/name-conflict-fixes.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/bootstrap/bootstrap.bundle.min.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/js.cookie.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.validate.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery-ui-timepicker-addon.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/jquery/jquery.debounce-1.0.6.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/menu_resizer.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/cross_framing_protection.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/messages.php?l=ru&v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/config.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/doclinks.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/functions.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/navigation.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/indexes.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/common.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/page_settings.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/lib/codemirror.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/mode/sql/sql.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/runmode/runmode.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/hint/show-hint.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/hint/sql-hint.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/codemirror/addon/lint/lint.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/codemirror/addon/lint/sql-lint.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/vendor/tracekit.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/error_report.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/drag_drop_import.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/shortcuts_handler.js?v=5.2.0"></script>
  <script data-cfasync="false" type="text/javascript" src="js/dist/console.js?v=5.2.0"></script>

<script data-cfasync="false" type="text/javascript">
// <![CDATA[
CommonParams.setAll({common_query:"",opendb_url:"index.php?route=/database/structure",lang:"ru",server:"1",table:"",db:"",token:"5166214022615d26215e33513f7c2a75",text_dir:"ltr",LimitChars:"50",pftext:"",confirm:true,LoginCookieValidity:"1440",session_gc_maxlifetime:"3600",logged_in:false,is_https:false,rootPath:"/openserver/phpmyadmin/",arg_separator:"&",version:"5.2.0",auth_type:"cookie",user:"root"});
var firstDayOfCalendar = '0';
var themeImagePath = '.\/themes\/bootstrap\/img\/';
var mysqlDocTemplate = '.\/url.php\u003Furl\u003Dhttps\u00253A\u00252F\u00252Fdev.mysql.com\u00252Fdoc\u00252Frefman\u00252F5.7\u00252Fen\u00252F\u002525s.html';
var maxInputVars = 1000;

if ($.datepicker) {
  $.datepicker.regional[''].closeText = '\u0413\u043E\u0442\u043E\u0432\u043E';
  $.datepicker.regional[''].prevText = '\u041F\u0440\u0435\u0434';
  $.datepicker.regional[''].nextText = '\u0421\u043B\u0435\u0434\u0443\u044E\u0449\u0438\u0439';
  $.datepicker.regional[''].currentText = '\u0421\u0435\u0433\u043E\u0434\u043D\u044F';
  $.datepicker.regional[''].monthNames = [
    '\u042F\u043D\u0432\u0430\u0440\u044C',
    '\u0424\u0435\u0432\u0440\u0430\u043B\u044C',
    '\u041C\u0430\u0440\u0442',
    '\u0410\u043F\u0440\u0435\u043B\u044C',
    '\u041C\u0430\u0439',
    '\u0418\u044E\u043D\u044C',
    '\u0418\u044E\u043B\u044C',
    '\u0410\u0432\u0433\u0443\u0441\u0442',
    '\u0421\u0435\u043D\u0442\u044F\u0431\u0440\u044C',
    '\u041E\u043A\u0442\u044F\u0431\u0440\u044C',
    '\u041D\u043E\u044F\u0431\u0440\u044C',
    '\u0414\u0435\u043A\u0430\u0431\u0440\u044C',
  ];
  $.datepicker.regional[''].monthNamesShort = [
    '\u042F\u043D\u0432',
    '\u0424\u0435\u0432',
    '\u041C\u0430\u0440',
    '\u0410\u043F\u0440',
    '\u041C\u0430\u0439',
    '\u0418\u044E\u043D',
    '\u0418\u044E\u043B',
    '\u0410\u0432\u0433',
    '\u0421\u0435\u043D',
    '\u041E\u043A\u0442',
    '\u041D\u043E\u044F',
    '\u0414\u0435\u043A',
  ];
  $.datepicker.regional[''].dayNames = [
    '\u0412\u043E\u0441\u043A\u0440\u0435\u0441\u0435\u043D\u044C\u0435',
    '\u041F\u043E\u043D\u0435\u0434\u0435\u043B\u044C\u043D\u0438\u043A',
    '\u0412\u0442\u043E\u0440\u043D\u0438\u043A',
    '\u0421\u0440\u0435\u0434\u0430',
    '\u0427\u0435\u0442\u0432\u0435\u0440\u0433',
    '\u041F\u044F\u0442\u043D\u0438\u0446\u0430',
    '\u0421\u0443\u0431\u0431\u043E\u0442\u0430',
  ];
  $.datepicker.regional[''].dayNamesShort = [
    '\u0412\u0441',
    '\u041F\u043D',
    '\u0412\u0442',
    '\u0421\u0440',
    '\u0427\u0442',
    '\u041F\u0442',
    '\u0421\u0431',
  ];
  $.datepicker.regional[''].dayNamesMin = [
    '\u0412\u0441',
    '\u041F\u043D',
    '\u0412\u0442',
    '\u0421\u0440',
    '\u0427\u0442',
    '\u041F\u0442',
    '\u0421\u0431',
  ];
  $.datepicker.regional[''].weekHeader = '\u041D\u0435\u0434.';
  $.datepicker.regional[''].showMonthAfterYear = true;
  $.datepicker.regional[''].yearSuffix = '';
  $.extend($.datepicker._defaults, $.datepicker.regional['']);
}

if ($.timepicker) {
  $.timepicker.regional[''].timeText = '\u0412\u0440\u0435\u043C\u044F';
  $.timepicker.regional[''].hourText = '\u0427\u0430\u0441';
  $.timepicker.regional[''].minuteText = '\u041C\u0438\u043D\u0443\u0442\u0430';
  $.timepicker.regional[''].secondText = '\u0421\u0435\u043A\u0443\u043D\u0434\u0430';
  $.extend($.timepicker._defaults, $.timepicker.regional['']);
}

function extendingValidatorMessages () {
  $.extend($.validator.messages, {
    required: '\u042D\u0442\u043E\u0020\u043F\u043E\u043B\u0435\u0020\u043D\u0435\u043E\u0431\u0445\u043E\u0434\u0438\u043C\u043E',
    remote: '\u0418\u0441\u043F\u0440\u0430\u0432\u044C\u0442\u0435\u0020\u044D\u0442\u043E\u0020\u043F\u043E\u043B\u0435',
    email: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u044B\u0439\u0020\u0430\u0434\u0440\u0435\u0441\u0020\u044D\u002D\u043F\u043E\u0447\u0442\u044B',
    url: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u044B\u0439\u0020URL',
    date: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u0443\u044E\u0020\u0434\u0430\u0442\u0443',
    dateISO: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u0443\u044E\u0020\u0434\u0430\u0442\u0443\u0020\u0028ISO\u0029',
    number: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u043E\u0435\u0020\u0447\u0438\u0441\u043B\u043E\u0432\u043E\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435',
    creditcard: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u044B\u0439\u0020\u043D\u043E\u043C\u0435\u0440\u0020\u043A\u0440\u0435\u0434\u0438\u0442\u043D\u043E\u0439\u0020\u043A\u0430\u0440\u0442\u044B',
    digits: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u0442\u043E\u043B\u044C\u043A\u043E\u0020\u0446\u0438\u0444\u0440\u044B',
    equalTo: '\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u0442\u043E\u0020\u0436\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435\u0020\u0435\u0449\u0435\u0020\u0440\u0430\u0437',
    maxlength: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043D\u0435\u0020\u0431\u043E\u043B\u0435\u0435\u0020\u007B0\u007D\u0020\u0441\u0438\u043C\u0432\u043E\u043B\u0028\u0430\/\u043E\u0432\u0029'),
    minlength: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043D\u0435\u0020\u043C\u0435\u043D\u0435\u0435\u0020\u007B0\u007D\u0020\u0441\u0438\u043C\u0432\u043E\u043B\u0028\u0430\/\u043E\u0432\u0029'),
    rangelength: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435\u0020\u043C\u0435\u0436\u0434\u0443\u0020\u007B0\u007D\u0020\u0438\u0020\u007B1\u007D\u0020\u0441\u0438\u043C\u0432\u043E\u043B\u0430\u043C\u0438\u0020\u0434\u043B\u0438\u043D\u043E\u0439'),
    range: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435\u0020\u043C\u0435\u0436\u0434\u0443\u0020\u007B0\u007D\u0020\u0438\u0020\u007B1\u007D\u0020\u0441\u0438\u043C\u0432\u043E\u043B\u0430\u043C\u0438'),
    max: $.validator.format('\u0412\u0432\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435\u0020\u043C\u0435\u043D\u044C\u0448\u0435\u0435\u0020\u0438\u043B\u0438\u0020\u0440\u0430\u0432\u043D\u043E\u0435\u0020\u007B0\u007D'),
    min: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435,\u0020\u0431\u043E\u043B\u044C\u0448\u0435\u0435\u0020\u0438\u043B\u0438\u0020\u0440\u0430\u0432\u043D\u043E\u0435\u0020\u007B0\u007D'),
    validationFunctionForDateTime: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u0443\u044E\u0020\u0434\u0430\u0442\u0443\u0020\u0438\u043B\u0438\u0020\u0432\u0440\u0435\u043C\u044F'),
    validationFunctionForHex: $.validator.format('\u0412\u0432\u0435\u0434\u0438\u0442\u0435\u0020\u043F\u0440\u0430\u0432\u0438\u043B\u044C\u043D\u043E\u0435\u0020\u0437\u043D\u0430\u0447\u0435\u043D\u0438\u0435\u0020HEX'),
    validationFunctionForMd5: $.validator.format('This\u0020column\u0020can\u0020not\u0020contain\u0020a\u002032\u0020chars\u0020value'),
    validationFunctionForAesDesEncrypt: $.validator.format('These\u0020functions\u0020are\u0020meant\u0020to\u0020return\u0020a\u0020binary\u0020result\u003B\u0020to\u0020avoid\u0020inconsistent\u0020results\u0020you\u0020should\u0020store\u0020it\u0020in\u0020a\u0020BINARY,\u0020VARBINARY,\u0020or\u0020BLOB\u0020column.')
  });
}

ConsoleEnterExecutes=false

AJAX.scriptHandler
  .add('vendor/jquery/jquery.min.js', 0)
  .add('vendor/jquery/jquery-migrate.js', 0)
  .add('vendor/sprintf.js', 1)
  .add('ajax.js', 0)
  .add('keyhandler.js', 1)
  .add('vendor/jquery/jquery-ui.min.js', 0)
  .add('name-conflict-fixes.js', 1)
  .add('vendor/bootstrap/bootstrap.bundle.min.js', 1)
  .add('vendor/js.cookie.js', 1)
  .add('vendor/jquery/jquery.validate.js', 0)
  .add('vendor/jquery/jquery-ui-timepicker-addon.js', 0)
  .add('vendor/jquery/jquery.debounce-1.0.6.js', 0)
  .add('menu_resizer.js', 1)
  .add('cross_framing_protection.js', 0)
  .add('messages.php', 0)
  .add('config.js', 1)
  .add('doclinks.js', 1)
  .add('functions.js', 1)
  .add('navigation.js', 1)
  .add('indexes.js', 1)
  .add('common.js', 1)
  .add('page_settings.js', 1)
  .add('vendor/codemirror/lib/codemirror.js', 0)
  .add('vendor/codemirror/mode/sql/sql.js', 0)
  .add('vendor/codemirror/addon/runmode/runmode.js', 0)
  .add('vendor/codemirror/addon/hint/show-hint.js', 0)
  .add('vendor/codemirror/addon/hint/sql-hint.js', 0)
  .add('vendor/codemirror/addon/lint/lint.js', 0)
  .add('codemirror/addon/lint/sql-lint.js', 0)
  .add('vendor/tracekit.js', 1)
  .add('error_report.js', 1)
  .add('drag_drop_import.js', 1)
  .add('shortcuts_handler.js', 1)
  .add('console.js', 1)
;
$(function() {
        AJAX.fireOnload('vendor/sprintf.js');
        AJAX.fireOnload('keyhandler.js');
        AJAX.fireOnload('name-conflict-fixes.js');
      AJAX.fireOnload('vendor/bootstrap/bootstrap.bundle.min.js');
      AJAX.fireOnload('vendor/js.cookie.js');
            AJAX.fireOnload('menu_resizer.js');
          AJAX.fireOnload('config.js');
      AJAX.fireOnload('doclinks.js');
      AJAX.fireOnload('functions.js');
      AJAX.fireOnload('navigation.js');
      AJAX.fireOnload('indexes.js');
      AJAX.fireOnload('common.js');
      AJAX.fireOnload('page_settings.js');
                    AJAX.fireOnload('vendor/tracekit.js');
      AJAX.fireOnload('error_report.js');
      AJAX.fireOnload('drag_drop_import.js');
      AJAX.fireOnload('shortcuts_handler.js');
      AJAX.fireOnload('console.js');
  });
// ]]>
</script>

  <noscript><style>html{display:block}</style></noscript>
</head>
<body id=loginform>
  
  
  

  
  
  
  

  <div id="page_content">
    

    
    <div class="modal fade" id="previewSqlModal" tabindex="-1" aria-labelledby="previewSqlModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="previewSqlModalLabel">Loading</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
      </div>
      <div class="modal-body"></div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
      </div>
    </div>
  </div>
</div>

    <div class="modal fade" id="enumEditorModal" tabindex="-1" aria-labelledby="enumEditorModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="enumEditorModalLabel">Редактор ENUM/SET</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
      </div>
      <div class="modal-body"></div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" id="enumEditorGoButton" data-bs-dismiss="modal">Вперёд</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
      </div>
    </div>
  </div>
</div>

    <div class="modal fade" id="createViewModal" tabindex="-1" aria-labelledby="createViewModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg" id="createViewModalDialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="createViewModalLabel">Создать представление</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
      </div>
      <div class="modal-body"></div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" id="createViewModalGoButton">Вперёд</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
      </div>
    </div>
  </div>
</div>

<div class="container">
<div class="row">
<div class="col-12">
<a href="./url.php?url=https%3A%2F%2Fwww.phpmyadmin.net%2F" target="_blank" rel="noopener noreferrer" class="logo">
<img src="./themes/bootstrap/img/logo_right.png" id="imLogo" name="imLogo" alt="phpMyAdmin" border="0">
</a>
<h1>Добро пожаловать в <bdo dir="ltr" lang="en">phpMyAdmin</bdo></h1>

<noscript>
<div class="alert alert-danger" role="alert">
  <img src="themes/dot.gif" title="" alt="" class="icon ic_s_error"> Для полноценной работы необходимо включить JavaScript!
</div>

</noscript>

<div class="hide" id="js-https-mismatch">
<div class="alert alert-danger" role="alert">
  <img src="themes/dot.gif" title="" alt="" class="icon ic_s_error"> Существует несоответствие между HTTPS, указанным на сервере и клиенте. Это может привести к неработоспособному phpMyAdmin или угрозе безопасности. Исправьте конфигурацию своего сервера, чтобы правильно указать HTTPS.
</div>

</div>





  <div class='hide js-show'>
    <div class="card mb-4">
      <div class="card-header">
        <span id="languageSelectLabel">
          Язык                                  <i lang="en" dir="ltr">(Language)</i>
                  </span>
      </div>
      <div class="card-body">
        <form method="get" action="index.php?route=/" class="disableAjax">
          <input type="hidden" name="route" value="/export"><input type="hidden" name="token" value="5166214022615d26215e33513f7c2a75">
          <select name="lang" class="form-select autosubmit" lang="en" dir="ltr" id="languageSelect" aria-labelledby="languageSelectLabel">
                          <option value="sq">Shqip - Albanian</option>
                          <option value="ar">&#1575;&#1604;&#1593;&#1585;&#1576;&#1610;&#1577; - Arabic</option>
                          <option value="hy">Հայերէն - Armenian</option>
                          <option value="az">Az&#601;rbaycanca - Azerbaijani</option>
                          <option value="bn">বাংলা - Bangla</option>
                          <option value="be">&#1041;&#1077;&#1083;&#1072;&#1088;&#1091;&#1089;&#1082;&#1072;&#1103; - Belarusian</option>
                          <option value="bg">&#1041;&#1098;&#1083;&#1075;&#1072;&#1088;&#1089;&#1082;&#1080; - Bulgarian</option>
                          <option value="ca">Catal&agrave; - Catalan</option>
                          <option value="zh_cn">&#20013;&#25991; - Chinese simplified</option>
                          <option value="zh_tw">&#20013;&#25991; - Chinese traditional</option>
                          <option value="cs">Čeština - Czech</option>
                          <option value="da">Dansk - Danish</option>
                          <option value="nl">Nederlands - Dutch</option>
                          <option value="en">English</option>
                          <option value="en_gb">English (United Kingdom)</option>
                          <option value="et">Eesti - Estonian</option>
                          <option value="fi">Suomi - Finnish</option>
                          <option value="fr">Fran&ccedil;ais - French</option>
                          <option value="gl">Galego - Galician</option>
                          <option value="de">Deutsch - German</option>
                          <option value="el">&Epsilon;&lambda;&lambda;&eta;&nu;&iota;&kappa;&#940; - Greek</option>
                          <option value="he">&#1506;&#1489;&#1512;&#1497;&#1514; - Hebrew</option>
                          <option value="hu">Magyar - Hungarian</option>
                          <option value="id">Bahasa Indonesia - Indonesian</option>
                          <option value="ia">Interlingua</option>
                          <option value="it">Italiano - Italian</option>
                          <option value="ja">&#26085;&#26412;&#35486; - Japanese</option>
                          <option value="kk">Қазақ - Kazakh</option>
                          <option value="ko">&#54620;&#44397;&#50612; - Korean</option>
                          <option value="nb">Norsk - Norwegian</option>
                          <option value="pl">Polski - Polish</option>
                          <option value="pt">Portugu&ecirc;s - Portuguese</option>
                          <option value="pt_br">Portugu&ecirc;s (Brasil) - Portuguese (Brazil)</option>
                          <option value="ro">Rom&acirc;n&#259; - Romanian</option>
                          <option value="ru" selected>&#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081; - Russian</option>
                          <option value="si">&#3523;&#3538;&#3458;&#3524;&#3517; - Sinhala</option>
                          <option value="sk">Sloven&#269;ina - Slovak</option>
                          <option value="sl">Sloven&scaron;&#269;ina - Slovenian</option>
                          <option value="es">Espa&ntilde;ol - Spanish</option>
                          <option value="sv">Svenska - Swedish</option>
                          <option value="tr">T&uuml;rk&ccedil;e - Turkish</option>
                          <option value="uk">&#1059;&#1082;&#1088;&#1072;&#1111;&#1085;&#1089;&#1100;&#1082;&#1072; - Ukrainian</option>
                          <option value="vi">Tiếng Việt - Vietnamese</option>
                      </select>
        </form>
      </div>
    </div>
  </div>

<form method="post" id="login_form" action="index.php?route=/" name="login_form" class="disableAjax hide js-show">
    <input type="hidden" name="route" value="/export"><input type="hidden" name="token" value="5166214022615d26215e33513f7c2a75">
  <input type="hidden" name="set_session" value="4h16oibeqtua10msr9l9n9b07sbkvpt9">
  
  <div class="card mb-4">
    <div class="card-header">
      Авторизация      <a href="./doc/html/index.html" target="documentation"><img src="themes/dot.gif" title="Документация" alt="Документация" class="icon ic_b_help"></a>
    </div>
    <div class="card-body">
      
      <div class="row mb-3">
        <label for="input_username" class="col-sm-4 col-form-label">
          Пользователь:        </label>
        <div class="col-sm-8">
          <input type="text" name="pma_username" id="input_username" value="root" class="form-control" autocomplete="username">
        </div>
      </div>

      <div class="row">
        <label for="input_password" class="col-sm-4 col-form-label">
          Пароль:        </label>
        <div class="col-sm-8">
          <input type="password" name="pma_password" id="input_password" value="" class="form-control" autocomplete="current-password">
        </div>
      </div>

              <input type="hidden" name="server" value="1">
          </div>
    <div class="card-footer">
              <input class="btn btn-primary" value="Авторизация" type="submit" id="input_go">
          </div>
  </div>
</form>


</div>



  </div>
  </body>
</html>
