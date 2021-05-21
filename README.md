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
    sandbox="allow-scripts allow-top-navigation"
    loading=lazy
    src="https://circle.comfi.es/f/example.com/"
    style=border:none;height:50px;width:300px;
></iframe>
```
