Hello World in Python on Cloud Foundry using Flask
================================================================================

This is a sample application showing how to deploy a simple hello world app
using Cloud Foundry and the Python build pack and demostrate the load balancing feature of Appfog.



To Use
================================================================================

```
cf push myappname
```

Replace myapp name with the name of your app (ex. hello-world)

[Deploy to Appfog](https://www.ctl.io/guides/appfog/deploy-an-application-to-appfog/)

To remove the app, login to Appfog using the cf command from the appfog page of the control portal:
Example: cf login -a https://api.useast.appfog.ctl.io -o ACCOUNT -u userid
Pick the space that the application is deployed and 'cf delete myappname'

license
================================================================================

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
