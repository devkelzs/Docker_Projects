# Official nodejs image
FROM node:18

# app directory
WORKDIR /app

# copy files into the container
COPY package.json ./
COPY app.js ./

#INSTALL dependencies
RUN npm install

# EXPOSE the port the app runs on
EXPOSE 3000

#START the app
CMD ["npm", "start"]