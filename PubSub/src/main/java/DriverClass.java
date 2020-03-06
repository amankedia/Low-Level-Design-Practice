public class DriverClass {

    public static void main(String[] args) {

        PubSubService pubSubService = new PubSubService();

        PublisherImpl javaPublisher = new PublisherImpl();
        PublisherImpl pythonPublisher = new PublisherImpl();

        SubscriberImpl javaSubscriber = new SubscriberImpl("JAVASUB");
        SubscriberImpl pythonSubscriber =  new SubscriberImpl("PYTHONSUB");
        SubscriberImpl allLanSubscriber = new SubscriberImpl("ALLSUB");

        Message javaMessage = new Message("java", "This is a Java message");
        Message javaMessage1 = new Message("java", "This is a Java1 message");
        Message javaMessage2 = new Message("java", "This is a Java2 message");

        Message pythonMessage = new Message("python", "This is a Python message");
        Message pythonMessage1 = new Message("python", "This is a Python message1");
        Message pythonMessage2 = new Message("python", "This is a Python message2");

        javaPublisher.publish(javaMessage, pubSubService);
        javaPublisher.publish(javaMessage1, pubSubService);
        javaPublisher.publish(javaMessage2, pubSubService);

        pythonPublisher.publish(pythonMessage, pubSubService);
        pythonPublisher.publish(pythonMessage1, pubSubService);
        pythonPublisher.publish(pythonMessage2, pubSubService);

        javaSubscriber.addSubscriber("java", pubSubService);
        pythonSubscriber.addSubscriber("python", pubSubService);
        allLanSubscriber.addSubscriber("java", pubSubService);
        allLanSubscriber.addSubscriber("python", pubSubService);

        pubSubService.broadcast();

//        System.out.println("Messages of Java Subscriber are: ");
//        javaSubscriber.printMessages();
//
//        System.out.println("\nMessages of Python Subscriber are: ");
//        pythonSubscriber.printMessages();
//
//        System.out.println("\nMessages of All Languages Subscriber are: ");
//        allLanSubscriber.printMessages();

        //After broadcast the messagesQueue will be empty, so publishing new messages to server
        System.out.println("\nPublishing 2 more Java Messages...");
        Message javaMsg4 = new Message("java", "JSP and Servlets");
        Message javaMsg5 = new Message("java", "Struts framework");

        javaPublisher.publish(javaMsg4, pubSubService);
        javaPublisher.publish(javaMsg5, pubSubService);

//        javaSubscriber.getMessagesForSubscriberOfTopic("java", pubSubService);
        System.out.println("\nMessages of Java Subscriber now are: ");
        pubSubService.broadcast();
        javaSubscriber.printMessages();

    }
}
