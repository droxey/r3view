# r3view
r3view: real code, real collaboration, real time.

### Idea
   * To create a node-based educational tool utilizing class technologies paired with my prior experience writing @ https://framebuzz.com (US Patent US20140199046) in python. We use the same tech described in the patent, but choose not to time-shift the content, only providing real time updates. :)
   
### Tech
   * The main editor features websockets + multiplexing to create channels that groups of individual users can utilize to share data asyncronously in real time!
   * The rest of the site is written in Django 1.11. Why?
     * Quick to implement ORM and provided administrative interface.
     * Tight integration with PostgreSQL. PostgreSQL 9.6 features `JSONField`: this is used to store messages. Django ORM allows us to perform complex queries on JSONFields as though it's schema was defined in the model directly. In future versions of this product, I will utilize this pattern to provide a clickable `git tree` in the editor sidebar that can be easily updated on our end when the filesystem changes.
     
### Stack
    * Node
    * Django
    * Websockets
    * Love
    
### Dependencies
    * PostgreSQL 9.6
    * Python 3
    * Node

#### Final Notes
    * Total hours clocked: 22.75.
    * I promise I write prettier code than this :)
