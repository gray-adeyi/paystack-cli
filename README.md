# paystack cli

[![Downloads](https://static.pepy.tech/badge/paystack-cli)](https://pepy.tech/project/paystack-cli)
[![Downloads](https://static.pepy.tech/badge/paystack-cli/month)](https://pepy.tech/project/paystack-cli)
[![Downloads](https://static.pepy.tech/badge/paystack-cli/week)](https://pepy.tech/project/paystack-cli)

A command line app for interacting with [Paystack's](https://paystack.com/) API. Built with
[Typer](https://typer.tiangolo.com/) and [Pypaystack2](https://gray-adeyi.github.io/pypaystack2/)

![a picture of the utility in use](./paystack-cli.png)

## Installation

Binaries of paystack cli be found [here](https://github.com/gray-adeyi/paystack-cli/releases/tag/v0.2.1).
Alternatively, Paystack cli can be installed from pypi with pip as shown below.

```bash
pip install paystack-cli
```

## First time configurations

You're required to add your paystack integration secret key as your auth_key for the cli on first use as shown below

```bash
paystack config AUTH_KEY
```

This sets up your paystack cli for use in development mode if the test secret key is used. This auth_key can be
removed with `paystack reset`. Run `paystack --help` to see available commands

## Examples

### Retrieve a single transaction from your integration

```bash
paystack txn get-txns --pagination 1
```

Running the command above should yield a result similar to the dump shown below

```bash
Response(
    status_code=200,
    status=True,
    message='Transactions retrieved',
    data=[
        {
            'id': 3785557723,
            'domain': 'test',
            'status': 'success',
            'reference': '2769088ddc23d52947c8e845f6a6bbdebd987f457e97f71c',
            'amount': 30000,
            'message': None,
            'gateway_response': 'Approved',
            'paid_at': '2024-05-11T10:00:29.000Z',
            'created_at': '2024-05-11T10:00:27.000Z',
            'channel': 'card',
            'currency': 'NGN',
            'ip_address': None,
            'metadata': {'invoice_action': 'create'},
            'log': None,
            'fees': 450,
            'fees_split': None,
            'customer': {'id': 47948280, 'first_name': 'Gbenga', 'last_name': 'Adeyi', 'email': 'coyotedevmail@gmail.com', 'phone': '', 'metadata': None, 'customer_code': 'CUS_73cb3biedlkbe4a', 'risk_action': 'default'},
            'authorization': {
                'authorization_code': 'AUTH_w1renosr9o',
                'bin': '408408',
                'last4': '4081',
                'exp_month': '12',
                'exp_year': '2030',
                'channel': 'card',
                'card_type': 'visa ',
                'bank': 'TEST BANK',
                'country_code': 'NG',
                'brand': 'visa',
                'reusable': True,
                'signature': 'SIG_JOdryeujwrsZryg0Lkrg',
                'account_name': None
            },
            'plan': {},
            'split': {},
            'subaccount': {},
            'order_id': None,
            'paidAt': '2024-05-11T10:00:29.000Z',
            'createdAt': '2024-05-11T10:00:27.000Z',
            'requested_amount': 30000,
            'source': {'source': 'merchant_api', 'type': 'api', 'identifier': None, 'entry_point': 'charge'},
            'connect': None,
            'pos_transaction_data': None
        }
    ]
)
```

By default, the results you get from the cli is a `Response` object which is a `NamedTuple` returned
by [Pypaystack2](https://gray-adeyi.github.io/pypaystack2/). To get a json result, use the `--json`
flag.

```bash
paystack txn get-txns --pagination 1 --json
```

Running the command above should yield a result similar to the dump shown below

```bash
[{"id": 3785557723, "domain": "test", "status": "success", "reference": "2769088ddc23d52947c8e845f6a6bbdebd987f457e97f71c", "amount": 30000, "message": null, "gateway_response": "Approved", "paid_at": "2024-05-11T10:00:29.000Z", "created_at": 
"2024-05-11T10:00:27.000Z", "channel": "card", "currency": "NGN", "ip_address": null, "metadata": {"invoice_action": "create"}, "log": null, "fees": 450, "fees_split": null, "customer": {"id": 47948280, "first_name": "John", "last_name": "Doe", "email": 
"johndoe@example.com", "phone": "", "metadata": null, "customer_code": "CUS_73cb3biedlkbe4a", "risk_action": "default"}, "authorization": {"authorization_code": "AUTH_w1renosr9o", "bin": "408408", "last4": "4081", "exp_month": "12", "exp_year": "2030", 
"channel": "card", "card_type": "visa ", "bank": "TEST BANK", "country_code": "NG", "brand": "visa", "reusable": true, "signature": "SIG_JOdryeujwrsZryg0Lkrg", "account_name": null}, "plan": {}, "split": {}, "subaccount": {}, "order_id": null, "paidAt": 
"2024-05-11T10:00:29.000Z", "createdAt": "2024-05-11T10:00:27.000Z", "requested_amount": 30000, "source": {"source": "merchant_api", "type": "api", "identifier": null, "entry_point": "charge"}, "connect": null, "pos_transaction_data": null}]
```

## Source code

[https://github.com/gray-adeyi/paystack-cli](https://github.com/gray-adeyi/paystack-cli)

## Videos

* [Installing paystack cli on windows from binaries](https://youtu.be/N8TfuJJ9ycI?si=oFJM4hZQSbl5QBuH)
* [Installing paystack cli via pip on windows](https://youtu.be/JWWkTwER9xg?si=ZEdnFwSgaShkj7_H)
* [How to use paystack cli](https://youtu.be/GuYtyh1Ew5E?si=WQaBQshViLjawUft)