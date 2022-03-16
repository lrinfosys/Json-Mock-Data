import json
import random
import uuid
import gzip

jsonArray = []
STATUS_CHOICE = ["INITIATED", "PENDING_APPROVAL"]

for i in range(0, 100000):
    random_amount = round(random.uniform(0, 5000), 2)
    jsonArray.append(
        {
            "MessageType": "PaymentEvent",
            "ApplicationID": "MSO",
            "InstructionIdentification": "37191911539582",
            "EndToEndIdentification": "3120080330968676004353959427926121",
            "PaymentId": str(uuid.uuid4()).upper()[:8],
            "ConsentId": "UNUSED",
            "TransferType": "OB.US.WIRE_OUT",
            "DebtorAccount": {
                "SchemeName": "US.MS.MSWMAAccountNumber",
                "Identification": "8787-01-28 14:51:06.345696",
                "AccountHolderName": "Paul Kynerd",
                "SecondaryIdentification": "101-088851-267",
            },
            "CreditorAccount": {
                "SchemeName": "US.OBIE.ABARTN",
                "Identification": "021000021",
                "ACcountHolderName": "Jameel Reid",
                "SecondaryIdentification": "12345678901",
                "AccountHolderAddress": {
                    "AddressType": "MailTo",
                    "Department": "Accounts Payable",
                    "PostalCode": "52362",
                    "TownName": "East Berlin",
                    "CountrySubDivision": "NY",
                    "Country": "US",
                    "AddressLine": [
                        "1 Fake Street",
                        "2 Fake Street",
                        "3 Fake Street",
                        "4 Fake Street",
                        "5 Fake Street",
                        "6 Fake Street",
                        "7 Fake Street"
                    ],
                },
            },
            "Status": random.choice(STATUS_CHOICE),
            "MicroStatus": "Complete",
            "PaymentAmount": {
                "NumericAmount": random_amount,
                "CurrencyUnit": "USD"
            },
            "BaseEquivalent": {
                "NumericAmount": random_amount,
                "CurrencyUnit": "USD"
            },
            "Actor": {
                "Identifier": "Y7197",
                "Type": "ADVISOR",
                "FirstName": "Frodo",
                "LastName": "Baggins"
            },
            "ActorComment": "Some comment.",
            "ActionDateTime": "2022-03-14T02:11:20.695",
            "EntryDateTime": "2022-03-14T10:15:30",
            "WireDetails": {
                "WireProduct": "USD",
                "Fees": [
                    {
                        "FeeType": "WIRE_FEE",
                        "Amount": {
                            "NumericAmount": 10,
                            "CurrencyUnit": "USD"
                        },
                        "ChargedTo": "CLIENT",
                        "FeeWaived": "false"
                    },
                    {
                        "FeeType": "PREPAYMENT_FEE",
                        "Amount": {
                            "NumericAmount": 7.5,
                            "CurrencyUnit": "USD"
                        },
                        "ChargedTo": "BRANCH",
                        "FeeWaived": "true"
                    }
                ],
                "Memos": [
                    {
                        "Prefix": "Some Prefix 111",
                        "Text": "Some text 111"
                    },
                    {
                        "Prefix": "Some Prefix 222",
                        "Text": "Some text 222"
                    },
                    {
                        "Prefix": "Some Prefix 333",
                        "Text": "Some text 333"
                    }
                ],
                "IntermediaryBankDetails": {
                    "SchemeName": "US.OBIE.ABARTN",
                    "Identification": "ABA123",
                    "BankName": "INTERMEDIARY BANK INC.",
                },
                "SecondIntermediaryBankDetails": {
                    "SchemeName": "US.OBIE.SWIFTID",
                    "Identification": "SWIFT789",
                    "BankName": "SHADY BANK OF BAHAMAS INC",
                },
                "ReasonForWire": "This is my Reason"
            },
            "OutboundPaymentDetails": {
                "GroupId": "GROUP777",
                "EstimatedSendByDate": "2022-03-14",
                "EstimatedReceiveByDate": "2022-03-14"
            },
            "Signatures": {
                "Signatures": [
                    {
                        "SignedBy": "foundation",
                        "Timestamp": "2022-03-14T02:11:20.698",
                        "Token": "993349a661263d2",
                    }
                ]
            }
        }
    )

json_string = json.dumps(jsonArray)

print(json_string)

with open("json_data.json", "w") as outfile:
    outfile.write(json_string)