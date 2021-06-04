#!/bin/bash

curl $(APPLICATION_URL)/api/v1/admin/run-migrations?migrationkey=$(MIGRATION_KEY)