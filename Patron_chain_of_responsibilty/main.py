from document_handlers import ApprovalHandler1, ApprovalHandler2, ApprovalHandler3

def main():
    handler1 = ApprovalHandler1()
    handler2 = ApprovalHandler2()
    handler3 = ApprovalHandler3()

    handler1.set_successor(handler2)
    handler2.set_successor(handler3)

    document_list = ["Documento número 1", "Documento número 2", "Documento número 3", "Documento número 4"]

    for doc in document_list:
        print(f"Procesando el: {doc}")
        handler1.process_document(doc)

if __name__ == "__main__":
    main()