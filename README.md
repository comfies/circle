# circle
the /comfi.es/ webcircle

[Current members](https://github.com/comfies/circle/blob/master/sites.toml)

## Embedding examples

```html
<iframe
    id=webcircle
    sandbox=allow-top-navigation
    loading=lazy
    src="https://circle.comfi.es/f/<!--DOMAIN-->/"
    style=border:none;height:50px;width:300px;
></iframe>
```

Or a heavily contrived example using a future JSON api, with fallback to iframe if desired features arn't supported.

```html
<div id=webcircle>
    <noscript>
        <iframe
            sandbox=allow-top-navigation
            loading=lazy
            src="https://circle.comfi.es/f/<!--DOMAIN-->/"
            style=border:none;height:50px;width:300px;
        ></iframe>
    </noscript>
    <script nomodule>
        document.currentScript.insertAdjacentElement('beforebegin', (function(){
            let el = document.createElement('div');
            el.classList.add('yesscript');
            el.style.display='inline';
            el.innerHTML = document.currentScript.previousElementSibling.innerHTML;
            return el;
        })());
    </script>
    <script type="module">
        (async function(){
            const circle = await (await fetch('https://circle.comfi.es/json/<!--DOMAIN-->/')).json()
            /* Do stuff here */
        })();
    </script>
</div>
```

