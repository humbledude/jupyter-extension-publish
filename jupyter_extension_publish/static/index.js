define([
  'base/js/namespace'
], function(
  Jupyter
) {
  function load_ipython_extension() {

    var handler = function () {
      var xhr = new XMLHttpRequest();
      xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
          if (xhr.status == 200) {
            var res = xhr.responseText;
            alert('success : ' + res);
          } else {
            alert('error : ' + xhr.status);
          }
        }
      };
      xhr.open('GET', '/hello');
      xhr.send();
    };

    var action = {
      icon: 'fa-comment-o', // a font-awesome class used on buttons, etc
      help    : 'Show an alert',
      help_index : 'zz',
      handler : handler
    };
    var prefix = 'jupyter_extension_publish';
    var action_name = 'show-alert';

    var full_action_name = Jupyter.actions.register(action, action_name, prefix); // returns 'my_extension:show-alert'
    Jupyter.toolbar.add_buttons_group([full_action_name]);
  }

  return {
    load_ipython_extension: load_ipython_extension
  };
});
