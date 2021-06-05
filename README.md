# Django To Do App
## Description
I have created a To Do List using HTML, CSS, Python and Django.  Users can add, edit, delete and mark off any todo item.

## UX
### User Stories:
#### Implemented:
1. As a user, I would like to add an item to the list.
    - End User Goal: User is able to add an item to the list.
    - End Business Goal: Add item functionality working as expected.
    - Acceptance Criteria: User is able to add an item to the list.
    - Measurement Of Success: Check Manual Tests document.
    
2. As a user, I would like to edit an item on the list.
    - End User Goal: User is able to edit an item on the list.
    - End Business Goal: Edit item functionality working as expected.
    - Acceptance Criteria: User is able to edit an item on the list.
    - Measurement Of Success: Check Manual Tests document.
    
3. As a user, I would like to delete an item from the list.
    - End User Goal: User is able to delete an item from the list.
    - End Business Goal: Delete item functionality working as expected.
    - Acceptance Criteria: User is able to delete an item from the list.
    - Measurement Of Success: Check Manual Tests document.
    
4. As a user, I would like to stike off an item that is complete.
    - End User Goal: User is able to stike off an item that is complete.
    - End Business Goal: Complete item functionality working as expected.
    - Acceptance Criteria: User is able to stike off an item that is complete.
    - Measurement Of Success: Check Manual Tests document.
    
## Framework:
The framework used here to help with the reponsiveness of this app was Bootstrap.
I have also used Django to help create this app.

## Requirements:
Access to desktop, laptop, table or mobile devices.
Internet connection.

## Deployment 
### Deploying to Heroku:
1. Go to the Heroku website [here](https://id.heroku.com/login).
2. Sign Up or Sign In which will direct you to the dashboard.
3. Click on **New > Create new app**.
4. Enter app name and choose region then press **Create App**.
5. Go to **Settings > Reveal Config Vars**:
    - Enter Keys and their values.
6. In the CLI, login into Heroku by **heroku login -i**, where you will be asked to your enter email address and
    password.
7. If you have already created your Heroku app, you can remote to your local repository with the heroku git:remote command.
8. Set debug=False for deployment.
9. To deploy your app to Heroku, use the git push command to push the code from your local repository’s master branch to 
    your heroku remote.
10. When the build is complete, on the Heroku website, in the app click **Open App**.

[Deploying with Git](https://devcenter.heroku.com/articles/git)
