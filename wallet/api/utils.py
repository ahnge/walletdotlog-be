def check_and_save(wallet, serializer):
    init_amount = wallet.amount
    entry_amount = serializer.validated_data['amount']
    entry_type = serializer.validated_data['log_type']
    if entry_type == 'n':
        if init_amount > entry_amount:
            serializer.save(wallet=wallet)
        else:
            serializer.save(wallet=wallet, amount=init_amount)
    else:
        serializer.save(wallet=wallet)
