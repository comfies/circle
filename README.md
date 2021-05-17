# circle
The /comfy/ webcircle, look at our [current members](https://circle.comfi.es/)!

## How to Join

1. Be a member of /comfy/ (*we r invite only sorry, if you open a pull request and we think ur cool we might accept :]*)
2. Edit the `sites.toml` and append something along the lines of the following at the end of the file:
```ini
[[site]]
  # how your website will show up in the index
  id = "your.domain.com"
  # the actual link to your website
  url = "https://example.com"
  # (optional) if you would like to style the embed to match the style of your site, you can do so by adding a link to your custom css document
  css = "https://example.com/src/webcircle.css"
```
3. Put the embed on your website, examples of ways you can do it are shown below.
4. Done!

## Embedding examples

```html
<iframe
    id=webcircle
    sandbox=allow-top-navigation
    loading=lazy
    src="https://circle.comfi.es/f/example.com/"
    style=border:none;height:50px;width:300px;
></iframe>
```

Or a heavily contrived example using a ***future*** JSON api, with fallback to iframe if desired features arn't supported.

```html
<div id=webcircle>
    <noscript>
        <iframe
            sandbox=allow-top-navigation
            loading=lazy
            src="https://circle.comfi.es/f/example.com/"
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
            const circle = await (await fetch('https://circle.comfi.es/api/example.com.json')).json();
            /* Do stuff here */
        })();
    </script>
</div>
```

## API Reference

### `/api/list.json`
Returns the full list of domain ids.
```json
[
    "comfi.es",
    "dystopia.club",
    "zvava.org",
    "lllil.li"
    // etc...
]
```

### `/api/sites.json`
Returns the full list of site objects.
```json
[
    { "id": "comfi.es", ... },
    { "id": "dystopia.club", ... },
    { "id": "zvava.org", ... },
    { "id": "lllil.li", ... }
    // etc...
]
```

### `/api/domain.json`
Returns info about a domain id.
```json
{
    "id": "domain",                       // domain's id
    "url": "https://domain/",             // domain's full url
    "css": "https://domain/webcircle.css" // domain's css (if any)
}
```

### `/api/f/domain.json`
Returns the previous and next site objects in the circle along with some other info, useful for constructing custom embeds.
```json
{
    "home": "https://circle.comfi.es/",    // home of webcircle
    "css": "https://domain/webcircle.css", // domain's css (if any)
    // previous website in the circle
    "prev": {
        "id": "prev-domain",
        "url": "https://prev-domain/",
        "css": "https://prev-domain/webcircle.css",
    },
    // next website in the circle
    "next": {
        "id": "next-domain",
        "url": "https://next-domain/",
        "css": "https://next-domain/webcircle.css",
    }
}
```
