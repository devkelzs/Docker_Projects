FROM nginx:alpine 

#Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/index.html

# copy static files to nginx html directory
COPY website/ /usr/share/nginx/html/

# EXPOSE port 80
EXPOSE 80