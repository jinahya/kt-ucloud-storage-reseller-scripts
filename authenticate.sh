#!/bin/sh
authUser=$1
authKey=$2
authAccount=$3
if [[ -n $authAccount ]]
then
    authUser=$authAccount:$authUser
fi
echo "authUer: " $authUser

