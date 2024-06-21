puts ">>> Ruby / rendering covers..."


def render_cover(issueIndex, titleText, releaseDate)
  puts "        / rendering issue#{issueIndex} cover..."

  content = File.read "core.html"
  processed = content % {
    issueIndex: issueIndex,
    titleText: titleText,
    releaseDate: releaseDate,
  }

  kit = IMGKit.new(html)
  export = kit.to_file("./assets/covers/#{index}.png")
end


# TODO render covers for each file
