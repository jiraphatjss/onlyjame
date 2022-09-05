from behave import * 
from environment import *

@step('POST request OTP for register API with new email')
def step_impl(context):
    request_url = 'https://auth.dev.cryptoknights.games/email/request-register-otp'
    request_body = {'email':'jame@mailinator.com'}
    response = requests.post(request_url,json = request_body)
    global status_code
    status_code = response.status_code
    global response_json
    response_json = json.loads(response.text)
    global used_email
    used_email = request_body

@step('Status code should be 200')
def step_impl(context):
    assert status_code == 200

@step('Get OTP in email')
def step_impl(context):
    pass

@step('Response body returns ref_id data <ref_id>')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "ref_id",
            "resend_after",
            "expiry"
        ],
        "properties": {
            "ref_id": {
                "type":"string"
            },
            "resend_after": {
                "type":"string"
            },
            "expiry": {
                "type":"string"
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('Response body returns resend_after data <resend_after>')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "ref_id",
            "resend_after",
            "expiry"
        ],
        "properties": {
            "ref_id": {
                "type":"string"
            },
            "resend_after": {
                "type":"string"
            },
            "expiry": {
                "type":"string"
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('Response body returns expiry data <expiry>')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "ref_id",
            "resend_after",
            "expiry"
        ],
        "properties": {
            "ref_id": {
                "type":"string"
            },
            "resend_after": {
                "type":"string"
            },
            "expiry": {
                "type":"string"
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('POST request OTP for register API with existing email')
def step_impl(context):
    request_url = 'https://auth.dev.cryptoknights.games/email/request-register-otp'
    request_body = {'email':'jame000@mailinator.com'}
    response = requests.post(request_url,json = request_body)
    # response = requests.post(request_url,json = used_email)
    global status_code
    status_code = response.status_code
    global response_json
    response_json = json.loads(response.text)

@step('Status code should be 422')
def step_impl(context):
    assert status_code == 422


@step('Response body returns details "Duplicate email"')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "detail"
        ],
        "properties": {
            "detail": {
                "type":"string",
                "const":"Duplicate email"
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('POST request OTP for register API with empty string')
def step_impl(context):
    request_url = 'https://auth.dev.cryptoknights.games/email/request-register-otp'
    request_body = {'email':""}
    response = requests.post(request_url,json = request_body)
    global status_code
    status_code = response.status_code
    global response_json
    response_json = json.loads(response.text)

@step('Response body returns msg "value is not a valid email address"')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "detail"
        ],
        "properties": {
            "detail": {
                "type":"array",
                "items": {
                    "type":"object",
                    "required": [
                        "loc",
                        "msg",
                        "type"
                    ],
                    "properties": {
                        "loc": {
                            "type":"array",
                            "items": {
                                "type":"string"
                            }
                        },
                        "msg": {
                            "type":"string",
                            "const":"value is not a valid email address"
                        },
                        "type": {
                            "type":"string",
                            "const":"value_error.email"
                        }
                    }
                }
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('Response body returns type "value_error.email"')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "detail"
        ],
        "properties": {
            "detail": {
                "type":"array",
                "items": {
                    "type":"object",
                    "required": [
                        "loc",
                        "msg",
                        "type"
                    ],
                    "properties": {
                        "loc": {
                            "type":"array",
                            "items": {
                                "type":"string"
                            }
                        },
                        "msg": {
                            "type":"string",
                            "const":"value is not a valid email address"
                        },
                        "type": {
                            "type":"string",
                            "const":"value_error.email"
                        }
                    }
                }
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('POST request OTP for register API with wrong format email')
def step_impl(context):
    request_url = 'https://auth.dev.cryptoknights.games/email/request-register-otp'
    request_body = {'email':"test"}
    response = requests.post(request_url,json = request_body)
    global status_code
    status_code = response.status_code
    global response_json
    response_json = json.loads(response.text)

@step('POST request OTP for register API without email key')
def step_impl(context):
    request_url = 'https://auth.dev.cryptoknights.games/email/request-register-otp'
    request_body = {}
    response = requests.post(request_url,json = request_body)
    global status_code
    status_code = response.status_code
    global response_json
    response_json = json.loads(response.text)

@step('Response body returns msg "field required"')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "detail"
        ],
        "properties": {
            "detail": {
                "type":"array",
                "items": {
                    "type":"object",
                    "required": [
                        "loc",
                        "msg",
                        "type"
                    ],
                    "properties": {
                        "loc": {
                            "type":"array",
                            "items": {
                                "type":"string"
                            }
                        },
                        "msg": {
                            "type":"string",
                            "const":"field required"
                        },
                        "type": {
                            "type":"string",
                            "const":"value_error.missing"
                        }
                    }
                }
            }
        }
    }
    validate(instance=response_json, schema=schema)

@step('Response body returns type "value_error.missing"')
def step_impl(context):
    schema = {
        "type":"object",
        "required": [
            "detail"
        ],
        "properties": {
            "detail": {
                "type":"array",
                "items": {
                    "type":"object",
                    "required": [
                        "loc",
                        "msg",
                        "type"
                    ],
                    "properties": {
                        "loc": {
                            "type":"array",
                            "items": {
                                "type":"string"
                            }
                        },
                        "msg": {
                            "type":"string",
                            "const":"field required"
                        },
                        "type": {
                            "type":"string",
                            "const":"value_error.missing"
                        }
                    }
                }
            }
        }
    }
    validate(instance=response_json, schema=schema)
    
    
