# DIGIT Lab Website

## View the website on your local machine

1. Follow the [instructions](https://gohugo.io/installation/) to install Hugo. Install Hugo with the version number v0.125.7. For example,

   ```bash
   CGO_ENABLED=1 go install -tags extended github.com/gohugoio/hugo@v0.125.7
   ```
   
2. Verify your Hugo version.

   ```bash
   hugo version
   ```
   
   If you get an error saying "Command 'hugo' not found," it is likely that the path of Hugo is not added to the PATH environment variable. To fix this, add the following line to `~/.bashrc`:
   
   ```
   export PATH=$PATH:<GOPATH>/bin
   ```
   Replace `<GOPATH>` with the path of Go, e.g., `$HOME/go`.
   
3. Start Hugo’s development server.
   
   ```bash
   hugo server -D
   ```
